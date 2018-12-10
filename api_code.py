#!/usr/bin/env python



import os
import sys
import json
from time import time
import requests

FARMWARE_NAME = 'API'
HEADERS = {
    'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
    'content-type': 'application/json'}



def data(value):
    
    message = 'Point x   is {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def get_point():
    """ ` """
    response = requests.get(
        os.environ['FARMWARE_URL'] + 'api/device',
        headers=HEADERS)
    try:
        #value = response.json()['args']['location']['args']['x']
	device_data = response.json()
	timezone_string = device_data['timezone']
	tz_offset_hours = device_data['tz_offset_hrs']
    except KeyError:
        tz_offset_hours = None
    if tz_offset_hours is None:
        data(5)
        sys.exit(0)
    else:
        data(tz_offset_hours)
        sys.exit(0)
    return tz_offset_hours


def post(wrapped_data):
    """Send the Celery Script command."""
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
                  data=payload, headers=HEADERS)

if __name__ == '__main__':
       data(5)
       sys.exit(0) 
       get_point()
    
