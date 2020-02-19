import requests
import json
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(), "logo.jpeg")


headers = {
	'content-type':'application/json',
	#"Authorization":"JWT "+ 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE1ODIxMzk1NjMsIm9yaWdfaWF0IjoxNTgyMTM5MjYzLCJlbWFpbCI6InJhaHVsc2hhcm1hY3M1MEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InJhaHVsIn0.wTiDVjqo3MaJFgDEZgQ6hriwFjUvTyyguXwqgtaVqE0',
}

data = {
	'username': 'amandeep1',
	'password': 'sR25012106',
	'password2': 'sR25012106',
	'email': 'amandeep1@rahul.com'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()#['token']
print(token)
#print(token)

# refresh_data = {
# 	'token':token
# }

# new_reponse = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_reponse.json()['token']
# print(new_token)


# get_endpoint = ENDPOINT + str(17)
# get_data = json.dumps({"id":1234})



# headers = {
# 	#"Content-Type":"application/json",
# 	"Authorization":"JWT "+token,
# }

# with open(image_path, 'rb') as image:
# 	file_data = {
# 		'image':image
# 	}

# 	data = {"content":"CONTENTS YAAR"}
# 	json_data = json.dumps(data)
# 	posted_response = requests.post(ENDPOINT, data=data, headers=headers, files=file_data)
# 	print(posted_response.text)


# r = requests.get(get_endpoint)
# print(r.text)




# r2 = requests.get(ENDPOINT)
# print(r2.status_code)





# post_headers = {
# 	'content-type':'application/json'
# }
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)

# print(post_response.text)



# def do_img(method ='get', data={}, is_json=True, img_path= None):
# 	headers = {}
# 	if is_json:
# 		headers['content-type'] = 'application/json'
# 		data = json.dumps(data)

# 	if img_path is not None:
# 		with open(image_path, 'rb') as image:
# 			file_data = {
# 				'image':image
# 			}
# 			r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
# 	else:
# 		r = requests.request(method, ENDPOINT, data=data, headers= headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r


# do_img(method='post', data={'user':1, "content": ""}, is_json=False, img_path=image_path)


# def do(method ='get', data={}, is_json=True):
# 	headers = {}
# 	if is_json:
# 		headers['content-type'] = 'application/json'
# 		data = json.dumps(data)
# 	r = requests.request(method, ENDPOINT, data=data, headers= headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r



#do(data={'id':8})
#do(method='delete', data={'id':8})
#do(method='put', data={'id':14, "content":"some cool new content and shit", "user":1})