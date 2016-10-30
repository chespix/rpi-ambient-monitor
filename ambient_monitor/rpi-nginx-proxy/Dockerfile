FROM resin/rpi-raspbian
MAINTAINER Ludovic Roguet <code@fourteenislands.io>

# libgcrypt20-dev
RUN \
  apt-get update && \
  apt-get install -y -q --no-install-recommends ca-certificates git mercurial golang nginx wget && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Fix for long server names
RUN sed -i 's/# server_names_hash_bucket/server_names_hash_bucket/g' /etc/nginx/nginx.conf

# Install docker-gen
ENV DOCKER_GEN_VERSION 0.7.3
RUN \
  wget https://github.com/jwilder/docker-gen/releases/download/${DOCKER_GEN_VERSION}/docker-gen-linux-armhf-$DOCKER_GEN_VERSION.tar.gz && \
  tar -C /usr/local/bin -xvzf docker-gen-linux-armhf-$DOCKER_GEN_VERSION.tar.gz && \
  rm /docker-gen-linux-armhf-$DOCKER_GEN_VERSION.tar.gz

# Install Forego
ENV GOPATH /opt/go
ENV PATH $PATH:$GOPATH/bin
RUN go get -u github.com/ddollar/forego

ADD data/ /app
WORKDIR /app

ENV DOCKER_HOST unix:///tmp/docker.sock

VOLUME ["/etc/nginx/certs"]

CMD ["forego", "start", "-r"]
