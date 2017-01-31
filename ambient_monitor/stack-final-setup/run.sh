#!/bin/bash
## simple script just tries until it curls and exits.
CLEAN=1
while [ $CLEAN -ne 0 ]
do
  CLEAN=0
  curl -X POST http://influxdb:8086/query --data-urlencode 'q=CREATE DATABASE ambient_metrics'
  CLEAN=$(($CLEAN + $?))
  curl http://${GF_SECURITY_ADMIN_USER}:${GF_SECURITY_ADMIN_PASSWORD}@grafana-service:3000/api/datasources -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"name":"influx","type":"influxdb","url":"http://influxdb:8086","access":"proxy","isDefault":true,"database":"ambient_metrics"}'
  CLEAN=$(($CLEAN + $?))
sleep 10
done
exit 0
