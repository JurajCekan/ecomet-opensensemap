#!/usr/bin/env python3

# Ecomet
from  ecomet_i2c_sensors.hdc1080 import hdc1080
from  ecomet_i2c_sensors.ms5637 import ms5637

# Configuration
import config

# Opensensemap
import requests
import json

from time import sleep
  
sens_hdc1080 = hdc1080.HDC1080()
sens_ms5637  = ms5637.MS5637()


def opensensemap(sensor_id, value):
    url = 'https://api.opensensemap.org/boxes/' + str(config.SENSEBOX_ID) + '/' + sensor_id
    data = {'value': value}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)


while True:
    (temp, hmdt, _) = sens_hdc1080.both_measurement()
    (_, _, pressure, _) = sens_ms5637.measure (accuracy = 6) # ( temp_celsius, temp_fahrenheit, pressure, ret) 

    # Send data if SENSOR_ID is defined in config.py file
    if config.SENSEBOX_SENSOR_ID_PRESSURE:
        opensensemap(config.SENSEBOX_SENSOR_ID_PRESSURE, pressure)
    if config.SENSEBOX_SENSOR_ID_TEMPERATURE:
        opensensemap(config.SENSEBOX_SENSOR_ID_TEMPERATURE, temp)
    if config.SENSEBOX_SENSOR_ID_HUMIDITY:
        opensensemap(config.SENSEBOX_SENSOR_ID_HUMIDITY, hmdt)

    # sleep for 300 seconds (5minutes)
    try:
        sleep(300)
    except KeyboardInterrupt:
        print(f'The program was terminated by the user.')
