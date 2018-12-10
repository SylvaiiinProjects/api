#! /usr/bin/env python

#The API is used to access the database (plants, sequences, points, etc.).


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
	
def data(value):
    
    message = '[time] Timee  is {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def post(wrapped_data):
    """Send the Celery Script command."""
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
data=payload, headers=HEADERS)

data(tz_offset_hours)
