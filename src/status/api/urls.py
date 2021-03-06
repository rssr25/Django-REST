from django.contrib import admin
from django.urls import path, include

from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    #StatusCreateAPIView, 
    #StatusDetailAPIView,
    #StatusUpdateAPIView,
    #StatusDeleteAPIView
    )


urlpatterns = [
    
     path('', StatusAPIView.as_view()),                    #/api/status -> List
     path('<int:id>/', StatusAPIDetailView().as_view()),
     #path('create/'			  , StatusCreateAPIView.as_view()),      #/api/status/create -> Create
     #path('<int:pk>/'		  , StatusDetailAPIView.as_view()),      #/api/status/12/ -> Detail
     # path('<int:pk>/update/'  , StatusUpdateAPIView.as_view()),      #/api/status/12/update -> Update
     # path('<int:pk>/delete/'  , StatusDeleteAPIView.as_view()),      #/api/status/12/delete -> Delete

]


### START WITH ####
# /api/status -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete


###END WITH#### fewer end points using HTTP methods. 

# /api/status/ -> List (ALL CRUD)
# /api/status/ -> Detail (ALL CRUD)