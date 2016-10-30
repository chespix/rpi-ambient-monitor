#!/usr/bin/python

# Requirements:
# adafruit library installed:
# https://github.com/adafruit/Adafruit_Python_DHT
#
#

# Import libraries
import sys
import time
import datetime
import requests
import json
import RPi.GPIO as GPIO
import Adafruit_DHT

# Setup pins and sensor model
ambient_sensor = 11
ambient_pin = 4
moisture_pin = 7
light_pin = 8

# For now the source and individual name are hardcoded
data_source = "blackbox"
individual_name = "OGK"
# This vars will hold the values of the reading
# The units are:
# ambient_temp_value in C
# ambient_humid_value in %
# plant_moisture_value as a boolean. (wet or not)
# ambient_light_value in the capacitor charge value. *
# * Weird, but it can be read as follows:
#     near 0 full light, Near 400000 full dark

# Setup GPIO for moisture sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(moisture_pin, GPIO.IN)

# Function to get light sensor value
def light_value (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high or count is high enough that is dark
    #while (GPIO.input(pin_to_circuit) == GPIO.LOW and count < 5000):
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

# Function to get values
def get_values(sensor, pin, moist_p, light_p):
    # Get humidity and temp values from HDT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Get boolean value from moisture sensor
    if GPIO.input(moist_p):
        moisture = 0
    else:
        moisture = 1

    # Get capacitor value for light sensor
    light = light_value(light_p)
    #light = 0

    return humidity, temperature, moisture, light

# Function to load the values into a local influxDB
def push_values(humidity, temperature, moisture, light, data_source, individual_name):

    url = "http://localhost:8086/write?db=indoor_metrics"
    payload = "ambient_temp,source=blackbox value=" + str(int(temperature)) + \
        "\nambient_humid,source=blackbox value="  + str(int(humidity)) + \
        "\nambient_light,source=blackbox value="  + str(light) + \
        "\nplant_moisture,source="  + data_source + \
        ",individual=" + individual_name + \
        " value=" + str(moisture)

    r = requests.post(url,data=payload)
    return


# Function to print the values on the screen (will be deactivated eventually)
def show_values(humidity, temperature, moisture, light):
    # Print the values or error
    print"Fecha (ARG): " + str(datetime.datetime.now() - datetime.timedelta(hours=3))
    if humidity is not None and temperature is not None:
        print('Temp: {0:0.1f}*\nHumedad: {1:0.1f}%'.format(temperature, humidity))
    else:
        print('Nose pudo leer sensor de ambiente. Volver a intentar!')

    # How much is the light value? (near 0 full light, Near 400000 full dark)
    print("Luz: " + str(light))

    # Finall line
    print("")
    return

## We are going to try and exec the code, or exit in a clean way
try:
    # Main program

    # Get initial values
    ambient_humid_value, ambient_temp_value, plant_moisture_value, ambient_light_value = get_values(ambient_sensor, ambient_pin, moisture_pin, light_pin)

    # Push the values into DB
    push_values(ambient_humid_value,ambient_temp_value, plant_moisture_value, ambient_light_value, data_source, individual_name)

    # Print the values or error
    show_values(ambient_humid_value,ambient_temp_value, plant_moisture_value, ambient_light_value)

# If keyboard interrupt, cleanup pin setup
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()