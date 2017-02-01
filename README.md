# Raspberry PI ambient monitor with Docker
## A dockerized stack to monitor and store sensors data, using cheap sensors and a raspberry pi.

This project deploys a fully functional ambient monitoring stack. The same will sense for room temperature, room humidity, the presence of light in the room and soil moisture from various sources. It also provides a live feed of the room.
The data points are saved into an influxDB, and visualized using Grafana.

## Screenshots
![Hardware Screenshot placeholder](/images/rpi_wiring.png?raw=true "RPI wiring")

![Dashboard Screenshot placeholder](/images/dashboard.png?raw=true "Grafana Dashboard")

## Requirements
1. A raspberry PI 3 or better (It might work on RPI 2, but I haven't tested).
2. The raspberry must have an OS with Docker and docker-compose installed. I recommend using the [hypriot raspberry pi OS image.](https://blog.hypriot.com/downloads/)
3. An RPI compatible web-cam (I'm using a [logitech c210](http://support.logitech.com/product/webcam-c210)).
4. The (cheap) sensors:
  * [Photo Cell (light sensor).](https://www.sparkfun.com/products/9088)
  * [Soil Moisture sensor.](https://www.sparkfun.com/products/13322)
  * [DHT11 temp and humidity sensor.](https://www.adafruit.com/product/386)

## Setup (DOCUMENTATION IN PROGRESS)
### Schematics
The sensor connections is pretty basic. You have to connect the DTH11 to RPI GPIO 4, the Soil Moisture sensor to RPO GPIO 7 and finally the Photo Cell to GPIO 8 with a 1uf pull down resistor. In order to modify the PIN assignation or to have more than one Soil Moisture sensor you need to review and modify the setup variables for the [sense.py](ambient_monitor/dockerfiles/rpi-sensing/sense.py) python script. More info on this in the [Fine Tuning section](#fine_tuning).
<br>
Finally connect the USB camera to any of the USB ports in the raspberry pi.
<br><br>
![Hardware Schematics placeholder](/images/schematics.png?raw=true "RPI schematics")
### Base setup

### Stack startup

### <a name="fine_tuning"></a>Fine tuning
If you want to dive deep into the config and fine tune it, I will suggest to start with:
[I'm a relative reference to a repository file](../blob/master/LICENSE)

