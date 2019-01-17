#! /usr/bin/env python

#The API is used to access the database (plants, sequences, points, etc.).


'Get specific data (such as timezone) from the FarmBot Web App.'

import os
import json
import requests

HEADERS = {
    'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
    'content-type': 'application/json'}

headers = {'Authorization': 'Bearer ' + os.environ['API_TOKEN'],
           'content-type': "application/json"}

#get device info
#response = requests.get(os.environ['FARMWARE_URL']+ 'api/device', headers=headers)
#device_data = response.json()

#get points
res = requests.get('https://my.farmbot.io/api/points', headers=headers)
points = res.json()


"""récupère les coordonnées x,y,z des points de la web app dans une liste"""
"""
coord=[]
for i in range(len(points)):
	coord.append(points[i]['x'])
	coord.append(points[i]['y'])
	coord.append(points[i]['z'])"""
	

#sortedpoints = sorted(points, key=lambda elem: (int(elem['x']), int(elem['y'])))

# Device timezone info (set via the dropdown in the Web App Device widget)
#timezone_string = device_data['timezone']
#tz_offset_hours = device_data['tz_offset_hrs']
	
def data(value):
    
    message = '[time] Time  is {}.'.format(value)
    wrapped_message = {
        'kind': 'send_message',
        'args': {
            'message_type': 'info',
            'message': message}}
    post(wrapped_message)

def post(wrapped_data):
    """Send the Celery Script command."""
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script', data=payload, headers=HEADERS)

if __name__=='__main__':
	data(coord)
	#data(tz_offset_hours)
