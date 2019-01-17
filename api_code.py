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


def api_post(endpoint, data):
        """POST to an API endpoint."""
        response = requests.post('https://my.farmbot.io/api/' + endpoint, headers=headers, json=json.dumps(data))
        return response.json()


def api_put(endpoint, data):
        response = requests.put('https://my.farmbot.io/api/'+ endpoint, headers=headers, data=json.dumps(data))
        return response.json()

def no_data(value):
    
    message = '[Points] Points are {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def post(wrapped_data):
    
    payload = json.dumps(wrapped_data) 
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
   data=payload, headers=HEADERS)
   
  
#api_put('farmware_envs', { name: 'new product name' })
#response = requests.get('https://my.farmbot.io/' + 'api/farmware_envs', headers=headers)
response = requests.put('https://my.farmbot.io/' + 'api/device/325', headers=headers, data=json.dumps({  "name": "Carrot Overlord"}))
response = requests.get('https://my.farmbot.io/' + 'api/device', headers=headers)
bot_state = response.json()
#posx = bot_state['location_data']['position']['x']

no_data(bot_state)


