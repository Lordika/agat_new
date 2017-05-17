from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^task/(?P<task_id>[0-9]+)', views.TasksView),
    url(r'^', views.index),
]
