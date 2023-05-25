from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import * 
from .serializers import * 
from .forms import * 


footer = Footer.objects.all()

def homeView(request):
    banner = Banner.objects.order_by('-posicao')
    noticias = Noticia.objects.order_by('-data')
    context={'banner':banner, 'noticias':noticias, 'footer':footer}
    return render(request, 'index.html', context)

@login_required
def alunoView(request):
    video = Video.objects.order_by('-data')
    context={'video':video, 'footer':footer}
    return render(request, 'area-do-aluno.html', context)





   
        