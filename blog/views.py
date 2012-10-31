#-*-coding:utf8-*-
# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

import datetime

from models import Artigo
from forms import FormArtigo

def index(request):
    html = "<h1>Estamos na index</h1>"
    return HttpResponse(html)

def olamundo(request):
    now = datetime.datetime.now()
    html = "<html><body>Ola mundo!<br/>Agora é %s.</body></html>" %now
    return HttpResponse(html)

def parametros(request, param):
    try:
        param = int(param)
    except ValueError:
        raise Http404()

    html = "Valor do parametro é %s " %param
    return HttpResponse(html)

def lista(request):

    lista_artigos = Artigo.objects.all()
    return render_to_response("lista.html", {'lista_artigos':lista_artigos})

def novo(request):
        if(request.method=="POST"):
            form = FormArtigo(request.POST, request.FILES)
            if form.is_valid():
                dados = form.cleaned_data
                artigo = Artigo(
                    titulo = dados['titulo'],
                    conteudo = dados['conteudo'],
                    publicacao = datetime.datetime.now()
                )

                artigo.save()
                return render_to_response("salvo.html",{})

        else:
            form = FormArtigo()

        return render_to_response("novo.html", {'form':form}, context_instance=RequestContext(request))

def artigo(request, id_artigo):
    artigo = Artigo.objects.get(pk=id_artigo)
    return render_to_response("artigo.html",{'artigo':artigo})


