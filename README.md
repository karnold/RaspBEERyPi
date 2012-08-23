RaspBEERyPi
===========

RasBEERyPi is a Django project for monitoring the fermentation process of home brew beer with the Raspberry Pi

# Overview

The goal of this project is to utilize the GPIO pins of the Raspberry Pi to monitor temperature and gravity
during the fermentation process of beer.  Our hypothesis is that the gravity can be measured utilizing a liquid
level sensor that is afixed to a hydrometer.  Readings from the liquid level sensor and an analog temperature
sensor will be utilized and logged to a database during fermentation.  Logged data will be available to be
viewed via command line and web interface tools provided by this package.

This project is experimental and is subject to change.  We will be blogging our progress at http://indianacraftbeer.com.  
Be sure to follow our updates to see how this comes to fruiton.

# Parts List

* Raspberry Pi
* Adafruit Pi Cobbler
* MCP3008 8-Channel 10-Bit Anolog to Digital Converter With SPI Interface
* TMP36 Analog Temperature sensor
* 8" eTape Liquid Level Sensor
* Standard issue hydrometer
