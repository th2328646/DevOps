"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Platform.views import *

urlpatterns = [
    url(r'^monitor/$', monitor, name='monitor'),
    url(r'^monitor/log_query/$', log_query, name='log_query'),
    url(r'^monitor/app_deploy/$', app_deploy, name='app_deploy'),
    url(r'^monitor/app_deploy/a.php$', php_test, name='app_deploy'),
    url(r'^deploy/upload/$', upload_file, name='upload_file'),
    url(r'^monitor/dev_monitor/$', dev_monitor, name='dev_monitor'),
    url(r'^monitor/dev_monitor/detail/', server_detail, name='server_detail'),
    url(r'^server/delete/$', server_delete, name='server_delete'),
    url(r'^server/add/', server_add, name='server_add'),
    url(r'^server/edit/', server_edit, name='server_edit'),
    url(r'^log/(?P<log_name>errlog.\d{4}-\d{2}-\d{2}.txt)/$', read_log, name='read_log'),
]
