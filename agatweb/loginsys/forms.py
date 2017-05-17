from django.contrib.auth import authenticate
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django import forms
from django.contrib.auth import login

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя', error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput, error_messages={'required': 'Укажите пароль'})

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None