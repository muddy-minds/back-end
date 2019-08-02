# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from django.conf.urls import url
from . import api

# router = DefaultRouter()


# app_name = 'adv'

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]