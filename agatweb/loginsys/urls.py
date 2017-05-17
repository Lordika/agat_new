from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/', views.log_in),
    url(r'^logout/', views.log_out),
]
