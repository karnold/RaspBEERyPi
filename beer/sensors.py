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
    ANALOG_GRAVITY  = 1

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
        pprint.pprint(adcout)

        return adcout

    def readTemp(self):
	temp = self.readadc(self.ANALOG_TEMP)
	celsius = ((1000 * (temp * (3.3 / 1023))) - 500) / 10
	fahrenheit = (celsius * 1.8) + 32
        return (celsius, fahrenheit)

    def readGravity(self):
        return self.readadc(self.ANALOG_GRAVITY)
