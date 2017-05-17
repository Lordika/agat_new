from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from loginsys.forms import LoginForm

from .models import Task


def index(request):
    form = LoginForm()
    tasks_list = Task.objects.all()
    if 'login_error' in request.GET:
        return render(request, 'generator/index.html', {'form': form, 'login_error': 'Ошибка', 'tasks_list': tasks_list})
    return render(request, 'generator/index.html', {'form': form, 'tasks_list': tasks_list})


def TasksView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return HttpResponse("You're voting on question %s." % task_id)
