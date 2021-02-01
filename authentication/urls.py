from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'auth'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', signup, name='signup'),
]
