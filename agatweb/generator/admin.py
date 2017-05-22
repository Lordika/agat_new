from django.contrib import admin

# Register your models here.
from .models import Task, GenTask, TaskIcon

admin.site.register(Task)
admin.site.register(GenTask)
admin.site.register(TaskIcon)
