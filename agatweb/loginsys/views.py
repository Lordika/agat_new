from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

from .forms import LoginForm
# Create your views here.


def log_in(request):
    form = LoginForm(request.POST)
    error_valid = {}
    if form.is_valid():
        if form.get_user():
            login(request, form.get_user())
    else:
        return redirect('/?login_error=login')
    return redirect('/', error_valid)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')