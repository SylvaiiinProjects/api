#!/usr/bin/env python

"""Save sensor value."""

import os
import sys
import json
from time import time
import requests

FARMWARE_NAME = 'API'
HEADERS = {
    'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
    'content-type': 'application/json'}

"""def get_input_env():
    prefix = FARMWARE_NAME        
    input_title = os.environ.get(prefix+"_pin")
    return input_title"""


""" 64 is always taken """


def no_data():
    
    message = '[Soil sensor Value] Pin {} value is not available.'.format(PIN)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'error',
            'message': message}}
    post(wrapped_message)

def data(value):
    
    message = '[Soil sensor Value] Pin {} value  is {}.'.format(PIN,value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def get_pin_value():
    """ Sequence `Read Pin` """
    response = requests.get(
        os.environ['FARMWARE_URL'] + 'api/v1/bot/state',
        headers=HEADERS)
    try:
        value = response.json()['pins']['64']['value']
    except KeyError:
        value = None
    if value is None:
        no_data()
        sys.exit(0)
    else:
        data(value)
        sys.exit(0)
    return value




def post(wrapped_data):
    """Send the Celery Script command."""
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
                  data=payload, headers=HEADERS)

if __name__ == '__main__':
    PIN = 64   
   
    get_pin_value()
    
