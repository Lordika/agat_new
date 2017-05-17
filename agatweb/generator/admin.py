from django.contrib import admin

# Register your models here.
from .models import Task, GenTask

admin.site.register(Task)
admin.site.register(GenTask)