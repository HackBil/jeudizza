# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('orders.views',
    url(r'^orders/$', 'orders'),
)
