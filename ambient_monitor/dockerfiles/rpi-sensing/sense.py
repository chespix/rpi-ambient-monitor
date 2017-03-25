#!/usr/bin/python

# Requirements:
# adafruit library installed:
# https://github.com/adafruit/Adafruit_Python_DHT
# Driver for lux sensor:
# https://github.com/lexruee/tsl2561
# python libraries installed:
# pip install requests
# pip install rpi.gpio

# Import libraries
import sys
import time
import datetime
import requests
import json
import RPi.GPIO as GPIO
import Adafruit_DHT
from tentacle_pi.TSL2561 import TSL2561


# InfluxDB URL and DB name
influxdb_url = "http://influxdb:8086"
influxdb_db = "ambient_metrics"

# Setup pins and sensor model
ambient_sensor = 11
ambient_pin = 4
moisture_pins = [7] # Remember to set the individual name for each pin in next section

# For now the source and individual names are hardcoded
data_source = "blackbox"
individual_names_by_pin =  {7: 'AUTOS'}


# This vars will hold the values of the reading
# The units are:
# ambient_temp_value in C
# ambient_humid_value in %
# plant_moisture_value as a boolean. (wet or not)
# ambient_light_value in Lux

# Setup GPIO for moisture sensor
GPIO.setmode(GPIO.BCM)
for pin in moisture_pins:
    GPIO.setup(pin, GPIO.IN)

# Setup i2c light sensor
tsl = TSL2561(0x39,"/dev/i2c-1")
tsl.enable_autogain()
#tsl.set_gain(0x08)
tsl.set_time(0x00)


# Function to get light sensor value
def light_value ():

    #Output of i2c light sensor
    return tsl.lux()

# Function to get values
def get_values(sensor, pin, moist_pins):
    # Get humidity and temp values from HDT11 sensor
    humidity = None
    while humidity is None or temperature is None:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # For each moisture sensor get boolean value
    moistures = {}
    for sensor in moist_pins:
        if GPIO.input(sensor):
            moistures[sensor] = 0
        else:
            moistures[sensor] = 1

    # Get capacitor value for light sensor
    light = light_value()

    return humidity, temperature, moistures, light

# Function to load the values into a local influxDB
def push_values(humidity, temperature, moistures, light, data_source, individual_names_by_pin):

    # Add general ambient info
    url = influxdb_url + "/write?db=" + influxdb_db
    payload = "ambient_temp,source=" + data_source + \
       " value=" + str(int(temperature)) + \
        "\nambient_humid,source=blackbox value="  + str(int(humidity)) + \
        "\nambient_light,source=blackbox value="  + str(light)
    r = requests.post(url,data=payload)

    #Add individual info
    for pin, moisture in moistures.items():
        payload = "plant_moisture,source="  + data_source + \
            ",individual=" + individual_names_by_pin[pin] + \
            " value=" + str(moisture)
        r = requests.post(url,data=payload)
    return


# Function to print the values on the screen (will be deactivated eventually)
def show_values(humidity, temperature, moistures, light):
    # Print the values or error
    print"Fecha (ARG): " + str(datetime.datetime.now() - datetime.timedelta(hours=3))
    if humidity is not None and temperature is not None:
        print('Temp: {0:0.1f}*\nHumedad: {1:0.1f}%'.format(temperature, humidity))
    else:
        print('Nose pudo leer sensor de ambiente. Volver a intentar!')

    # How much is the light value?
    print("Lux: " + str(light))

    #show individual info
    for pin, moisture in moistures.items():
        payload = "plant_moisture,source="  + data_source + \
            ",individual=" + individual_names_by_pin[pin] + \
            " value=" + str(moisture)
        print payload
    return

    # Finall line
    print("")
    return

## We are going to try and exec the code, or exit in a clean way
try:
    # Main program

    # Get initial values
    ambient_humid_value, ambient_temp_value, individuals_moisture_value, ambient_light_value = get_values(ambient_sensor, ambient_pin, moisture_pins)


    # Print the values or error
    show_values(ambient_humid_value,ambient_temp_value, individuals_moisture_value, ambient_light_value)

    # Push the values into DB
    push_values(ambient_humid_value,ambient_temp_value, individuals_moisture_value, ambient_light_value, data_source, individual_names_by_pin)


# If keyboard interrupt, cleanup pin setup
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
