#!/usr/bin/env python

import os
import requests
import json

headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}

FARMWARE_NAME = 'API'
HEADERS = {
    'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
'content-type': 'application/json'}


response = requests.get(os.environ['FARMWARE_URL'] + 'api/points',
              headers=headers)


def no_data(value):
    
    message = '[Points] Points are {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def post(wrapped_data):
    
    payload = json.dumps(wrapped_data) # convert string as object
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
   data=payload, headers=HEADERS)


bot_state = response.json()
#posx = bot_state['location_data']['position']['x']

no_data(bot_state)

