FROM hypriot/rpi-alpine-scratch
MAINTAINER Maximo Vazquez Brust
RUN echo "0.1" > /version
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*
COPY run.sh /run.sh
RUN chmod +x /run.sh
ENTRYPOINT ["/bin/sh", "/run.sh"]
