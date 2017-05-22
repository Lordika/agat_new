from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^download/(?P<task_id>[0-9]+)', views.DownloadTask),
    url(r'^gen/(?P<task_id>[0-9]+)', views.generation),
    url(r'^task/(?P<task_id>[0-9]+)', views.TasksView),
    url(r'^', views.index),
]
