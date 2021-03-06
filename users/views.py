from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, RegisterUserForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')
    lst_error = {
        'password1': 'Проверьте пароль',
        'password2': 'Проверьте пароль',
        'email': 'Проверьте почту',
        'username': 'Проверьте имя пользователя',
    }


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            if form.errors:
                for field, error in form.errors.items():
                    messages.error(request, f'{self.lst_error.get(field, "")}')
            else:
                messages.error(request, 'Не правильно заполнена форма. Проверьте '
                                    'данные!')
            return redirect(reverse_lazy('users:register'))

class UserLogoutView(LogoutView):
    template_name = 'main/index.html'