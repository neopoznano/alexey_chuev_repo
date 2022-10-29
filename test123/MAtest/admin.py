# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'http_url', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
