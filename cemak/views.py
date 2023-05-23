from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import * 
from .serializers import * 
from .forms import * 


def homeView(request):
    context={}
    return render(request, 'index.html', context)

@login_required
def alunoView(request):
    context={}
    return render(request, 'area-do-aluno.html', context)


def treinamentoView(request):
    context={}
    return render(request, '.html', context)



   
        