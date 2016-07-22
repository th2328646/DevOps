# -*- coding: UTF-8 -*-
import os
import json
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from Platform.libs.test import handle_uploaded_file
from forms import UploadFileForm
from models import Server


def log_query(request):
    if 'time' in request.GET:
        if request.GET['time']:
            require_time = request.GET['time']
            log_path = 'F:\log\errlog.%s.txt' % require_time
            if os.path.exists(log_path):
                f = open(log_path, 'r')
                content = f.readlines()
                return render_to_response('log_query.html', dict(time=require_time, logs=content[-100:]))
            else:
                e = 'err_log is not exist!'
                return render_to_response('log_query.html', dict(time=require_time, error=e))
    log_dir = os.listdir('F:\log')
    return render_to_response('log_query.html', dict(all_logs=json.dumps(log_dir)))


def read_log(request, log_name):
    path = os.path.join('F:\log', log_name)
    f = open(path, 'r')
    content = f.readlines()
    return render_to_response('show_log.html', dict(logs=content[-100:]))


def app_deploy(request):
    server = Server.objects.all()
    return render_to_response('app_deploy.html', dict(servers=server), context_instance=RequestContext(request))


def dev_monitor(request):
    server = Server.objects.all()
    return render_to_response('dev_monitor.html', dict(servers=server))


@csrf_exempt
def server_delete(request):
    if request.is_ajax() and request.method == 'POST':
        if 'ip' in request.POST:
            to_del = Server.objects.get(ip=request.POST['ip'])
        try:
            to_del.delete()
            return HttpResponse(True)
        except Exception, e:
            return e
    return HttpResponse('error')


@csrf_exempt
def server_add(request):
    if request.method == 'POST':
        try:
            Server.objects.create(hostname=request.POST['hostname'], ip=request.POST['ip'],
                                  description=request.POST['description'])
            server = Server.objects.all()
            return render_to_response('dev_monitor.html', dict(servers=server),
                                      context_instance=RequestContext(request))
        except Exception, e:
            return e
    return render(request, 'dev_monitor.html')


def server_detail(request):
    return render(request, 'server_detail.html')


@csrf_exempt
def server_edit(request):
    if request.method == 'POST':
        if 'ip' in request.POST and request.POST['ip']:
            try:
                to_edit = Server.objects.get(id=request.POST['id'])
                to_edit.hostname = request.POST['hostname']
                to_edit.ip = request.POST['ip']
                to_edit.description = request.POST['description']
                to_edit.save()
                server = Server.objects.all()
                return render_to_response('dev_monitor.html', dict(servers=server),
                                          context_instance=RequestContext(request))
            except Exception, e:
                return e
        return HttpResponse('Please input ip.')
    return render(request, 'dev_monitor.html')


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = handle_uploaded_file(request.FILES['file'])
            server = Server.objects.all()
            return render_to_response('app_deploy.html', dict(servers=server, names=name),
                                      context_instance=RequestContext(request))
        else:
            server = Server.objects.all()
            return render_to_response('app_deploy.html', dict(servers=server), context_instance=RequestContext(request))


def php_test(request):
    return HttpResponse(request)


def monitor(request):
    return render(request, 'monitor.html')
