# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Urls(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    http_url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.http_url
