from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

#def detail_view(request):
#	return render() # return JSON data or XML data. This is shortcut for HTTPResponse



def json_example_view(request):

	'''
	URI -- URI for a REST API
	GET -- retrieve
	'''
	data = {
		"count":1000,
		"content": "Some newer content"
	}

	return JsonResponse(data)