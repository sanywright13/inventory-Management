from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.base import TemplateView
# Create your views here.
class Index(TemplateView):
    template_name="inventory/index.html"