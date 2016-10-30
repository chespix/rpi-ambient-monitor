FROM resin/rpi-raspbian
MAINTAINER Maximo VB

RUN apt-get update && apt-get install -q -y --no-install-recommends \
  motion

VOLUME ["/var/lib/motion"]
COPY motion.conf /etc/motion/motion.conf
 

ENTRYPOINT ["/usr/bin/motion"]
