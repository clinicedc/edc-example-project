from django.conf import settings
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include
from django_collect_offline.admin_site import django_collect_offline_admin

from .admin_site import example_subject_admin

app_name = "example_subject"


urlpatterns = []
