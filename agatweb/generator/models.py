from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.


class Task(models.Model):
    Task_title = models.CharField(max_length=150)
    Task_info = models.CharField(max_length=150)

    def __str__(self):
        return self.Task_title


class GenTask(models.Model):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    file = models.FilePathField(path=os.path.join(os.path.abspath(os.getcwd()), 'static'), null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.taskId.pk)