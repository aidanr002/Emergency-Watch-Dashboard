from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView
from .modules import *
from django.views import generic

#http://emergencywatch.pythonanywhere.com/status/
class HomeView(ListView):
    template_name = "./core/view.home.html"
    context_object_name = 'module_status_list'

    def get_queryset(self):
        """Return the status of the modules."""
        return get_module_statuses()
