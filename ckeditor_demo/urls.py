from __future__ import absolute_import

import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles import views

from .demo_application.views import ckeditor_form_view

if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^$', ckeditor_form_view, name='ckeditor-form'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^ckeditor/', include('ckeditor.urls')),
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
else:
    from django.conf.urls import patterns

    admin.autodiscover()
    urlpatterns = patterns(
        '',
        url(r'^$', ckeditor_form_view, name='ckeditor-form'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^ckeditor/', include('ckeditor.urls')),
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
