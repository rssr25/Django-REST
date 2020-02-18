from django.contrib import admin
from django.urls import path, include


from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthView


urlpatterns = [
    path(''     , AuthView.as_view()),
    path('jwt/'     , obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
    # path('json/example/'			, json_example_view),
    # path('json/cbv/'				, JsonCBV.as_view()),
    # path('json/cbv2/'				, JsonCBV2.as_view()),
    # path('json/serialized/list/'	, SerializedListView.as_view()),
    # path('json/serialized/detail/'	, SerializedDetailView.as_view())
]