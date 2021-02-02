from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

from .forms import *


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request,f'Welcome {user.username}, You are now logged in.')
                    return redirect(reverse('lead:lead-list'))
                else:
                    messages.error(request,'Account is not active.')
                    return redirect(reverse('login'))
            else:
                messages.error(request,'Invalid Credentials.')
                return redirect(reverse('login'))
        messages.error(request, 'Invalid form values.')
        return render(request, 'authentication/login.html')


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('lead:lead-list')
