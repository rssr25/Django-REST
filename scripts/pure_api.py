import json 
import requests #http requests

BASE_URL = "http://127.0.0.1:8000/"
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

def create_update():

	new_data = {

		"user":1,
		"content": "Another more cool update yaasuj"
	}

	r = requests.post(BASE_URL + ENDPOINT, data = json.dumps(new_data))
	print(r.headers)

	if r.status_code == requests.codes.ok:
		#print(r.json())
		return r.json()
	return r.text

#get_list()

def do_obj_update():

	new_data = {
		"content": "New Obj Data"
	}

	r = requests.put(BASE_URL + ENDPOINT + "1/", data = json.dumps(new_data))
	print(r.status_code)

	if r.status_code == requests.codes.ok:
		#print(r.json())
		return r.json()
	return r.text


def do_obj_delete():

	new_data = {
		"content": "New Obj Data"
	}

	r = requests.delete(BASE_URL + ENDPOINT + "1/")
	print(r.status_code)

	if r.status_code == requests.codes.ok:
		#print(r.json())
		return r.json()
	return r.text

print(create_update())
