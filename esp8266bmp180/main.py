from bmp180 import BMP180
from machine import I2C, Pin                        # create an I2C bus object accordingly to the port you are using
import time

import network
try: 
    import usocket as socket
except:
    import socket

ssid = '<REDACTED>'
password = '<REDACTED>'

station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig(('192.168.1.104','255.255.255.0','192.168.1.1','192.168.1.1'))
station.config(dhcp_hostname="ESP_hall")
station.connect(ssid, password)


while station.isconnected() == False:
    pass

print("connected wifi")

#bus = I2C(1, baudrate=100000)           # on pyboard
bus =  I2C(scl=Pin(5), sda=Pin(4), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',8080))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)

    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print(temp, p, altitude)

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/plain; version=0.0.4; charset=utf-8')
    conn.send('Connection: close\n\n')
    conn.sendall('# HELP home_sensor_temperature_celcius Home temperature sensor reading\n# TYPE home_sensor_temperature_celcius gauge\nhome_sensor_temperature_celcius {}\n# HELP home_sensor_barpressure_pascal Home barometer pressure sensor reading\n# TYPE home_sensor_barpressure_pascal gauge\nhome_sensor_barpressure_pascal {}'.format(temp,p))
    conn.close()