#!/usr/bin/python3
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost',
                        port=8086,
                        username='',
                        password='')
line = 'power_info,sensor=motor1 power_in=123,power_out=348'
client.write([line], {'db': 'energy'}, 204, 'line')
client.close()

