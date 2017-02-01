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
5. A public DNS domain to access the service from the net (Optional)

## Setup
### Schematics
The sensor connections is pretty basic. You have to connect the DTH11 to RPI GPIO 4, the Soil Moisture sensor to RPO GPIO 7 and finally the Photo Cell to GPIO 8 with a 1uf pull down resistor. In order to modify the PIN assignation or to have more than one Soil Moisture sensor you need to review and modify the setup variables for the [sense.py](ambient_monitor/dockerfiles/rpi-sensing/sense.py) python script. More info on this in the [Fine Tuning section](#fine_tuning).
<br>
Finally connect the USB camera to any of the USB ports in the raspberry pi.
<br><br>
![Hardware Schematics placeholder](/images/schematics.png?raw=true "RPI schematics")
(The fritzing project file is available at the [fritzing folder](fritzing/))

### Base setup
You can run the stack as it is, but as a bare minimum you should modify the grafana and motion services passwords. By default, they are configured as `admin/admin`. If you wan to go with default credentials, and not planning on access the service through the web, you can jump directly to [Stack startup](#stack_startup) section.

#### Grafana credentials and FQDN
In order to update grafana credentials, edit the file [env.grafana](ambient_monitor/env.grafana) then update the environment variables to setup the admin username and password.
If you are planning to access the service through the web, you need to specify the FQDN of you service in the `GF_SERVER_DOMAIN` environment variable.

#### Motion credentials
In order to update the motion credentials, edit the file [motion.conf](ambient_monitor/motion-conf/motion.conf). Search for the following options, and update the stream and web control credentials:
```
stream_authentication admin:admin
webcontrol_authentication admin:admin
```

#### Grafana initial dashboard
Now we will update the grafana default dashboard to use the correct motion stream credentials.
In order to do so, edit the file [sensor_motion.json](ambient_monitor/grafana-dashboards/sensor_monitor.json), search for the above string, and update with your FQDN for the stream service, and the stream service credentials previously setup in motion conf. If you are not accessing the service from the web, you must use your docker host IP instead of the FQDN.
`<iframe src=\"https://admin:admin@camera.example.com/\"`

#### Nginx SSL certificate and key
If you are planning on accessing your ambient monitor service from the web, it is very important to setup SSL to keep your video feed and dashboard safe. In order to do so, you will need to generate your own SSL cert and key if you don't have one. You can follow the instructions on [this site](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs) to generate them.
Once you have your SSL cert and key, copy them to the folder [nginx-certs](ambient_monitor/nginx-certs) and name them as your base domain, as the example cert and key files placed on the directory.

#### Stack environment variables 
Finally you need to update the FQDN that will be used for accesing the services in the [env.stack](ambient_monitor/env.stack) file.

### <a name="stack_startup"></a>Stack startup
Once you have setup the environment, you only need to execute one command to bring up the service.
Place your prompt at [ambient_monitor](ambient_monitor/) folder inside this repo, and execute:

`# docker-compose up`

This should start up the whole stack.


If you have setup your domain to point to the docker-host, you should be ready to access the server through its FQDN.

If you havent setup SSL, you can access your grafana service at `http://docker-host-ip:3000` and your motion (live feed) service at `http://docker-host-ip:8081`.


### <a name="fine_tuning"></a>Fine tuning (WIP)
If you want to dive deep into the config and fine tune it, I will suggest to start with:
[I'm a relative reference to a repository file](../blob/master/LICENSE)

