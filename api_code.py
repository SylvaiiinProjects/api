#!/usr/bin/env python

import os
import json
import requests

headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}

def get_data():
	response = requests.get(os.environ['FARMWARE_URL'] + 'api/v1/bot/state',
              headers=headers)
	try:
	    bot_state = response.json()
            pin_64_value = bot_state['pins']['64']['value']
        except KeyError:
	    pin_64_value = None
        return pin_64_value


if __name__='__main__':
	get_data()
"""
'Get specific data (such as timezone) from the FarmBot Web App.'

import os
import json
import requests

headers = {'Authorization': 'Bearer ' + os.environ['API_TOKEN'],
           'content-type': "application/json"}
response = requests.get('https://my.farmbot.io/api/device', headers=headers)
device_data = response.json()

# Device timezone info (set via the dropdown in the Web App Device widget)

timezone_string = device_data['timezone']
tz_offset_hours = device_data['tz_offset_hrs']

"""
