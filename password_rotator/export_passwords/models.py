# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    host_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return 'HostName: %s UserName: %s Password: %s' % (self.host_name, self.username, self.password)