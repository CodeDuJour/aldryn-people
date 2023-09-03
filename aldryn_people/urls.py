# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import path

from aldryn_people.views import DownloadVcardView, GroupDetailView, GroupListView, PersonDetailView


urlpatterns = [
    path(r'group/(?P<pk>[0-9]+)/',
        GroupDetailView.as_view(), name='group-detail'),
    path(r'group/(?P<slug>[A-Za-z0-9_\-]+)/',
        GroupDetailView.as_view(), name='group-detail'),

    path(r'(?P<pk>[0-9]+)/',
        PersonDetailView.as_view(), name='person-detail'),
    path(r'(?P<slug>[A-Za-z0-9_\-]+)/',
        PersonDetailView.as_view(), name='person-detail'),

    path(r'(?P<pk>[0-9]+)/download/',
        DownloadVcardView.as_view(), name='download_vcard'),
    path(r'(?P<slug>[A-Za-z0-9_\-]+)/download/',
        DownloadVcardView.as_view(), name='download_vcard'),

    path(r'',
        GroupListView.as_view(), name='group-list'),
]
