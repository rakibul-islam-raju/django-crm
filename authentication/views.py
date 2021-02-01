from django.shortcuts import render, redirect, reverse
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
                    return redirect(reverse('auth:login'))
            else:
                messages.error(request,'Invalid Credentials.')
                return redirect(reverse('auth:login'))
        messages.error(request, 'Invalid form values.')
        return render(request, 'authentication/login.html')


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    # def get(self, request, *args, **kwargs):
    #     form = SignupForm()
    #     context = {
    #         'form': form
    #     }

    #     return render(request, 'registration/signup.html', context)

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request,f'Account successfully created for {username}')
            user = authenticate(username=username, password=user.password)
            login(request, user)
            messages.success(request,f'Welcome {username}, You are now logged in.')
            return redirect(reverse('lead:lead-list'))
        else:
            print(form.errors.as_data)
            messages.success(request,f'Invalid form values.')
        #     return redirect(reverse('auth:signup'))

        return render(request, 'registration/signup.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            form.save()
            messages.success(request,f'Account successfully created for {username}')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,f'Welcome {username}, You are now logged in.')
            return redirect(reverse('lead:lead-list'))
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})