from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
#from rest_framework.generics import ListAPIView

#from django.views.generic import View

from status.models import Status
from .serializers import StatusSerializer

#write views here

class StatusListSearchAPIView(APIView):

	permission_classes = []
	authentication_classes = []

	def get(self, request, format = None):
		qs = Status.objects.all()
		serializer = StatusSerializer(qs, many=True)
		return Response(serializer.data)


	def post(self, request, fromat = None):
		pass


#CreateModelMixin -- POST method
#UpdateModelMixin -- PUT method
#DestroyModelMixin -- DELETE method

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): #create list

	permission_classes 			= []
	authentication_classes 		= []
	serializer_class 			= StatusSerializer

	# def get(self, request, format = None):
	# 	qs = Status.objects.all()
	# 	serializer = StatusSerializer(qs, many=True)
	# 	return Response(serializer.data)

	def get_queryset(self):
		qs = Status.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains = query)

		return qs

	def post(self, request, *args, **kwargs):

		return self.create(request, *args, **kwargs)

	#def perform_create(self, serializer):
 	# 	serializer.save(user = self.request.user)


# class StatusCreateAPIView(generics.CreateAPIView):

# 	permission_classes 			= []
# 	authentication_classes 		= []
# 	queryset 					= Status.objects.all()
# 	serializer_class 			= StatusSerializer





class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):

	permission_classes 			= []
	authentication_classes 		= []
	queryset 					= Status.objects.all()
	serializer_class 			= StatusSerializer

	def put(self, request, *args, **kwargs):

		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):

		return self.destroy(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):

		return self.update(request, *args, **kwargs)


#cleaner version of above method
# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

# 	permission_classes 			= []
# 	authentication_classes 		= []
# 	queryset 					= Status.objects.all()
# 	serializer_class 			= StatusSerializer



# class StatusUpdateAPIView(generics.UpdateAPIView):

# 	permission_classes 			= []
# 	authentication_classes 		= []
# 	queryset 					= Status.objects.all()
# 	serializer_class 			= StatusSerializer
# 	#lookup_field 				= 'id'


# class StatusDeleteAPIView(generics.DestroyAPIView):

# 	permission_classes 			= []
# 	authentication_classes 		= []
# 	queryset 					= Status.objects.all()
# 	serializer_class 			= StatusSerializer
# 	#lookup_field 				= 'id'


