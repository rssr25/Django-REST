from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
import json

from cfeapi.mixins import JsonResponseMixin
from .models import Update

from django.core.serializers import serialize


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


class SerializedDetailView(JsonResponseMixin, View):

	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		data = serialize("json", [obj,], fields=('user', 'content'))

		return HttpResponse(data, content_type='application/json')


class SerializedListView(JsonResponseMixin, View):

	def get(self, request, *args, **kwargs):
		querySet = Update.objects.all()

		data = serialize("json", querySet, fields=('user', 'content'))
		# data = {
		# 	"user":obj.user.username,
		# 	"content":obj.content
		# }
		return HttpResponse(data, content_type='application/json')