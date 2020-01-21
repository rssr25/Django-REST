import json
from django.views.generic import View
from django.http import HttpResponse

from cfeapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin

from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm

from .utils import is_json





#creating, retrieving, updating, deleting (1) -- Update Model

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):

	'''
	Retrieve, Update, Delete --> Object
	'''

	is_json = True

	def get_object(self, id=None):

		print(id)
		try:
			obj = UpdateModel.objects.get(id=id)
		except UpdateModel.DoesNotExist:
			obj = None

		# qs = UpdateModel.objects.filter(id=id)
		# if qs.count == 1:
		# 	return qs.first()
		# return None
		return obj




	def get(self, request, id, *args, **kwargs):

		obj = self.get_object(id=id)
		#print(id)

		if obj is None:
			error_data = json.dumps({"message": "update not found"})
			return self.render_to_response(error_data, status=404)
		json_data = obj.serialize()

		return self.render_to_response(json_data)



	def post(self, request, *args, **kwargs):

		data = json.dumps({"message": "Not allowed, please use the /api/updates/ endpoint"})
		return self.render_to_response(data)
  


	def put(self, request, id, *args, **kwargs):

		valid_json = is_json(request.body)
		if not valid_json:
			error_data = json.dumps({"message" : "Invalid data sent, please send using JSON"})
			return self.render_to_response(error_data, status=400)


		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({"message": "update not found"})
			return self.render_to_response(error_data, status=404)


		data = json.loads(obj.serialize())
		passed_data = json.loads(request.body)

		for key, value in passed_data.items():
			data[key] = value

		form = UpdateModelForm(data)
		if form.is_valid():
			obj = form.save(commit = True)
			obj_data = json.dumps(data)

			return self.render_to_response(obj_data, status = 201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status = 400)

		data = json.dumps({"message":"something"})
		return self.render_to_response(data)


	def delete(self, request, id, *args, **kwargs):

		obj = self.get_object(id=id)

		if obj is None:
			error_data = json.dumps({"message": "Item not found"})
			return self.render_to_response(error_data, status=404)

		deleted_, item_deleted = obj.delete()
		print(deleted_)

		if deleted_ == 1:
			data = json.dumps({"message":"successfully deleted"})
			return self.render_to_response(data, status = 200)

		error_data - json.dumps({"message": "Could not delete item. Please try again later."})
		return self.render_to_response(data, status = 400)

class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):

	'''
	List View
	Create View

	'''

	is_json = True


	def get(self, request, *args, **kwargs):

		qs = UpdateModel.objects.all()
		json_data = qs.serialize()

		return self.render_to_response(json_data)
		

	def post(self, request, *args, **kwargs):\

		#print(request.POST)

		valid_json = is_json(request.body)
		if not valid_json:
			error_data = json.dumps({"message" : "Invalid data sent, please send using JSON"})
			return self.render_to_response(error_data, status=400)

		data = json.loads(request.body)
		form = UpdateModelForm(data)
		if form.is_valid():
			obj = form.save(commit = True)
			obj_data = obj.serialize()

			return self.render_to_response(obj_data, status = 201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status = 400)

		data = {"message":"Not Allowed"}
		return self.render_to_response(data, status = 400)


	def delete(self, request, *args, **kwargs):
		data = json.dumps({"message": "You cannot delete an entire list!"})
		return self.render_to_response(data, status = 403)






