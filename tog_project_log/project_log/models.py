from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    public = models.BooleanField(default=True)

    tags = TaggableManager()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
