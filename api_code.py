#! /usr/bin/env python

#The API is used to access the database (plants, sequences, points, etc.).

## GET

# Exemple 1

import os
import json
import requests
#from farmware_tools import app
#points = app.get('points')



headers = {'Authorization': 'Bearer ' + os.environ['API_TOKEN'],
           'content-type': "application/json"}

response = requests.get('https://my.farmbot.io/api/points', headers=headers)
points = response.json()['args']['location']['args']['x']

def post(wrapped_data):
    """Send the Celery Script command."""
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
                  data=payload, headers=headers)

def log(value):
    
    message = '[] point  is {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

if __name__=='__main__':
	log(5)
	#p=points(['x'])
	log(points)

"""
# Exemple 2
'Get specific data (such as timezone) from the FarmBot Web App.'

import os
import requests

headers = {'Authorization': 'Bearer ' + os.environ['API_TOKEN'],
           'content-type': "application/json"}
response = requests.get('https://my.farmbot.io/api/device', headers=headers)
device_data = response.json()

# Device timezone info (set via the dropdown in the Web App Device widget)
timezone_string = device_data['timezone']
tz_offset_hours = device_data['tz_offset_hrs']

print('My device timezone is: {} (UTC{})'.format(timezone_string, tz_offset_hours)) """
