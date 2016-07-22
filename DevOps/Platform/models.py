from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Server(models.Model):
    hostname = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.hostname, self.ip



