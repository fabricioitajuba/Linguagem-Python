#!/usr/bin/python3
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost',
                        port=8086,
                        username='',
                        password='',
                        database='energy')
result = client.query('SELECT * FROM "power_info"')
points = result.get_points(tags={'sensor': 'motor1'})
for point in points:
    print("Time: %s, power_in: %i, power_out: %i" \
          % (point['time'], point['power_in'], point['power_out']))
client.close()
