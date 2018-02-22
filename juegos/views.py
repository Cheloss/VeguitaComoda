# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from juegos.models import JuegosInflables
from django.shortcuts import render, get_object_or_404
from juegos.forms import NoticiaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def noticia_list(request):
    data = {}

    data['object_list'] = JuegosInflables.objects.all().order_by('-created')


    template_name = 'noticia/noticia_list.html'
    return render(request, template_name, data)
def noticia_update(request, pk) :
    data = {}

    data['object_list'] = JuegosInflables.objects.filter(pk=pk)
    template_name = 'noticia/noticia_detalle.html'
    return render(request, template_name, data)