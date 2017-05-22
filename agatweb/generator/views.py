from django.shortcuts import get_object_or_404, render, redirect
from loginsys.forms import LoginForm
from django.http import FileResponse, HttpResponse
import threading
import os

from .models import Task
from .gen import generation_task


def index(request):
    form = LoginForm()
    tasks_list = Task.objects.all()
    if 'login_error' in request.GET:
        return render(request, 'generator/index.html', {'form': form, 'login_error': 'Ошибка',
                                                        'tasks_list': tasks_list})
    return render(request, 'generator/index.html', {'form': form, 'tasks_list': tasks_list})


def TasksView(request, task_id):
    if not request.user.is_authenticated:
        return redirect('/')
    task = get_object_or_404(Task, pk=task_id)
    curtask = {'pass': 'generator/{}.html'.format(task.id), 'gen_pass': '/gen/{}/'.format(task_id)}
    tasks_list = Task.objects.all()
    return render(request, 'generator/index.html', {'tasks_list': tasks_list, 'task': curtask})


def generation(request, task_id):
    if not request.user.is_authenticated:
        return redirect('/')
    task = get_object_or_404(Task, pk=task_id)
    newTask = generation_task(request.user.last_name, request.user.first_name, task_id, request.user.id)
    thread = threading.Thread(target=newTask.gen)
    thread.start()
    return redirect('/task/{}/'.format(task_id))


def DownloadTask(request, task_id):
    if not request.user.is_authenticated:
        return redirect('/')
    task = get_object_or_404(Task, pk=task_id)
    path = os.path.join(os.path.abspath(os.getcwd()),  'static', 'Stud',
                        request.user.last_name + request.user.first_name, str(task_id), 'Task',
                        '{}{}{}'.format(request.user.last_name, request.user.first_name, '.pdf'))
    with open(path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=task.pdf'
        return response

