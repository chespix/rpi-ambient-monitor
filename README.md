# Raspberry PI ambient monitor with Docker
## A dockerized ambient sensor monitor stack, using cheap sensors and a raspberry pi.

This project deploys a fully functional ambient monitoring stack. The same will sense for room temperature, room humidity, the presence of light and soil moisture from various sources. It also provides a live feed of the room.
The data points are saved into an influxDB, and visualized using Grafana.

## Screenshots
![Hardware Screenshot placeholder](/screenshots/rpi_wiring.png?raw=true "RPI wiring")

![Dashboard Screenshot placeholder](/screenshots/dashboard.png?raw=true "Grafana Dashboard")


## Requirements
1. A raspberry PI 3 or better (It might work on RPI 2, but I haven tested).
2. The raspberry must have an OS with Docker and docker-compose installed. I recommend using the [hypriot raspberry pi OS image.](https://blog.hypriot.com/downloads/)
3. An RPI compatible web-cam (I'm using a [logitech c210](http://support.logitech.com/product/webcam-c210)).
4. The (cheap) sensors:
  * [Photo Cell (light sensor).](https://www.sparkfun.com/products/9088)
  * [Soil Moisture sensor.](https://www.sparkfun.com/products/13322)
  * [DHT11 temp and humidity sensor.](https://www.adafruit.com/product/386)

## Setup
### Schematics
![Hardware Schematics placeholder](/screenshots/schematics.png?raw=true "RPI schematics")
### Base setup
### Fine tuning
If you want to dive deep into the config and fine tune it, I will suggest to start with:
[I'm a relative reference to a repository file](../blob/master/LICENSE)

