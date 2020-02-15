"""为应用程序users定义URL模式"""

#from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlPatterns = [
    # 登录界面
    path('login/', LoginView.as_view, {'template_name': 'users/login.html'}, name='login'),
]