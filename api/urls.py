from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('auth/users/relationship/',
         views.RelationshipAPI.as_view(), name='followees'),
    path('auth/users/organization/',
         views.OrganizationAPI.as_view(), name='organization'),
]
