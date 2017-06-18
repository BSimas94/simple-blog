from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'
