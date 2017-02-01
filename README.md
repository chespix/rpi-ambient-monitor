# Raspberry PI ambient monitor with Docker 

This project deploys a fully functional ambient monitoring stack. The same will sense for room temperature, room humidity, the presence of light and soil moisture. It also provides a live feed of the room.
The data points are saved into an influxDB, and visualized using Grafana.

## Screenshots
![Dashboard Screenshot placeholder](/screenshots/dashboard.png?raw=true "Grafana Dashboard")
![Hardware Schematics placeholder](/screenshots/schematics.png?raw=true "RPI schematics")
![Hardware Screenshot placeholder](/screenshots/rpi_wiring.png?raw=true "RPI wiring")

## Requirements
1. A raspberry PI 3 or better (It might work on RPI 2, but I haven tested).
2. The raspberry must have an OS with Docker and docker-compose installed. I recommend using the hypriot raspberry pi OS image.
3. An RPI compatible web-cam (I'm using a logitech c210).
4. The (cheap) sensors:
..* https://www.sparkfun.com/products/9088 Photo Cell (light sensor).
..* https://www.sparkfun.com/products/13322 Soil Moisture sensor.
..* https://www.adafruit.com/product/386 DHT11 temp and humidity sensor.

## Setup
### Schematics
### Base setup
### Fine tuning
If you want to dive deep into the config and fine tune it, I will suggest to start with:

