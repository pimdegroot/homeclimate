# Home Climate

In this repo you can find my micropython code, Prometheus config and Grafana dashboard for my home climate monitoring. Hardware used is a wemos D1 mini (ESP8266) with a BMP180 temperature / barometer shield. Because of heattransfer the shield and the wemos are seperated by du-pont cables.

## Micropython
The code for the ESP connects to a wifi access point, starts a webserver and sends the temperature in Celcius and the air pressure in Pascal using a format Prometheus can parse. It does that on the IP address stated in station.ifconfig() at port 8080.

## Prometheus
The config file for Prometheus contains several endpoints. Adjust as needed.

## Grafana
The json in the grafana folder can be imported as a start for your own dashboard. It assumes the same endpoints are available as the Prometheus config. This also includes a special endpoint not included in this repo, containing a light sensor and humidity sensor, so remove graphs and queries as needed.


### Notes
This hobby project is considered finished as per June 2019. This repository is made available as a starting point for your own project. Although I am happy to hear what you have made using this information, I am unable to provide further support.