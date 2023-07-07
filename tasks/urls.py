from django.contrib import admin
from django.urls import path
from . import views

from mc.settings import STATIC_URL

urlpatterns = [
    path('', views.listTasks, name = 'listTasks'),
    path('new', views.nuevaTask, name = 'nuevaTask'),
]

