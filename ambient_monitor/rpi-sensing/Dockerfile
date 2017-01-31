FROM resin/rpi-raspbian:jessie
MAINTAINER Maximo Vazquez Brust <chespi@gmail.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install requests
RUN pip install rpi.gpio
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install
RUN cd / 
RUN cd / && git clone https://github.com/chespix/project.git

# Define working directory
WORKDIR /project

CMD ["/bin/bash"]
