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
        os.environ['FARMWARE_URL'] + 'api/points',
        headers=HEADERS)
    try:
        value = response.json()['args']['location']['args']['x']
    except KeyError:
        value = None
    if value is None:
        data(5)
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
        
       get_point()
    
