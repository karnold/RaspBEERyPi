import time
import os
import RPi.GPIO as GPIO

import pprint

GPIO.setmode(GPIO.BCM)
DEBUG = 1

class sensors:

    # Define our GPIO pins
    SPICLK  = 18
    SPIMISO = 23
    SPIMOSI = 24
    SPICS   = 25

    # define analog pins
    ANALOG_TEMP     = 7
    ANALOG_GRAVITY  = 6

    def __init__(self):
        GPIO.setup(self.SPIMOSI, GPIO.OUT)
        GPIO.setup(self.SPIMISO, GPIO.IN)
        GPIO.setup(self.SPICLK, GPIO.OUT)
        GPIO.setup(self.SPICS, GPIO.OUT)

    def readadc(self, adcnum):
        if (adcnum > 7) or (adcnum < 0):
            return -1

        GPIO.output(self.SPICS, True)
        GPIO.output(self.SPICLK, False)
        GPIO.output(self.SPICS, False)

        commandout = adcnum
        commandout |= 0x18 # start bit + single-ended bit
        commandout <<= 3 # we only need to send 5 bits

        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(self.SPIMOSI, True)
            else:
                GPIO(self.SPIMOSI, False)
            commandout <<= 1
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)

        adcout = 0

        # read in one empty bit, one null bit, and 10 ADC bits
        for i in range(12):
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)        
            adcout <<= 1
            if (GPIO.input(self.SPIMISO)):
                adcout |= 0x1

        GPIO.output(self.SPICS, True)

        adcout >>= 1 # first bit is null so drop it

        return adcout

    def readTemp(self):
        temp = self.readadc(self.ANALOG_TEMP)
        celsius = int(((1000 * (temp * (3.3 / 1023))) - 500) / 10)
        return celsius 

    def tempFahrenheit(self, temp):
        return int((temp * 1.8) + 32)

    def readGravity(self):
        curReading = self.readadc(self.ANALOG_GRAVITY)
        # Maximum Reading - Will need to be a calibrated setting in the future
        maxReding = 1000.0 # just taking a guess
        # Minimum Reading - Will need to be a calibrated setting in the future
        minReading = 250.0 # again, a guess
        # Range - Used in calculating percent
        range = maxReading - minReading
        # Sensor Length - We will need to find the length in Brix.
        length = 50 # just a place holder
        # Percent From top, or zero Brix.
        perFromTop= (curReading - minReading)/range
        # Reading in Brix.
        brixReading = length * perFromTop
        # Reading in SG.
        sgReading = 1.000898 + 0.003859118*brixReading + 0.00001370735*brixReading**2 + 0.00000003742517*brixReading**3
        # Get temp for temp correction
        curCTemp = self.readTemp()
        curFTemp = self.tempFahrenheit(curCTemp)
        # Temperature corrected SG
        correction = 1.313454 - 0.132674*curFTemp + 0.002057793*curFTemp**2 - 0.000002627634*curFTemp**3
        sgCorrected = sgReading + (correction * 0.001)
        return sgCorrected
