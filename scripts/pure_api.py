import json 
import requests #http requests

BASE_URL = "http://127.0.0.1:8001/"
ENDPOINT = "api/updates/"


def get_list():

	r = requests.get(BASE_URL + ENDPOINT)
	
	print(r.status_code)

	status_code= r.status_code
	if status_code != 200:
		print('probably not a good sign?')

	data = r.json() #converts to python list

	print(type(json.dumps(data))) #converts to python string

	for obj in data:
		if obj['id'] == 1:

			r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))

			print(r2.json())


#print(get_list())

get_list()