from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Task(models.Model):
    Task_title = models.CharField(max_length=150)
    Task_info = models.CharField(max_length=150)

    def __str__(self):
        return self.Task_title


class TaskIcon(models.Model):
    icon = models.CharField(max_length=25)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class GenTask(models.Model):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    icon = models.ForeignKey(TaskIcon, on_delete=models.CASCADE)
    instance = models.IntegerField()

    def __str__(self):
        return 'Работа пользователя {} №{} попытка №{}'.format(self.user, self.taskId.pk, int(self.instance))

    def print(self):
        return 'Попытка №{}'.format(int(self.instance))
