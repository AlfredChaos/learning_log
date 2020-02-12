"""定义myProjects的URL模式"""

from django.conf.urls import url
from . import views
from django.urls import path,re_path

app_name = 'myProjects'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]