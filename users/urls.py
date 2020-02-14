"""为应用程序users定义URL模式"""

#from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import login
from . import views

urlPatterns = [
    # 登录界面
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]