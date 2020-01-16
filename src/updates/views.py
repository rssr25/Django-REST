from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
import json

from cfeapi.mixins import JsonResponseMixin


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


class JsonCBV(View):

	def get(self, request, *args, **kwargs):

		'''
		URI -- URI for a REST API
		GET -- retrieve
		'''
		data = {
			"count":1000,
			"content": "Some newer content"
		}

		return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):

	def get(self, request, *args, **kwargs):

		data = {
			"count":1000,
			"content": "Some newer content"
		}

		return self.render_to_json_response(data)


