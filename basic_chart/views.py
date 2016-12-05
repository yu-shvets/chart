# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Region, Data
from django.views.generic import ListView, View, DetailView
from django.shortcuts import get_object_or_404
from urllib.parse import unquote

# Create your views here.


def index(request):

    current_region = unquote(request.COOKIES.get('current_region'))

    data = Data.objects.filter(region=current_region)

    regions = Region.objects.all()

    return render(request, 'index.html', {'data': data, 'regions': regions})


class RegionList(ListView):

    template_name = 'region_info.html'

    def get_queryset(self):

        return Data.objects.filter(region=self.args[0])

    def get_context_data(self, **kwargs):
        kwargs['regions'] = Region.objects.all()

        return super(RegionList, self).get_context_data(**kwargs)