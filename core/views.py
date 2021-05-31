from core.models import Evento
from django.shortcuts import render, HttpResponse

# Create your views here.

def localEvento(request, nome_evento):
    objeto = Evento.objects.get(titulo = nome_evento)
    return HttpResponse('O local do evento {} será em {}'.format(nome_evento, objeto.local))

def descricaoEvento(request, nome_evento):
    objeto = Evento.objects.get(titulo = nome_evento)
    return HttpResponse('A descricacao do evento {} é {}'. format(nome_evento, objeto.descricao))

def dataEvento(request, nome_evento):
    objeto = Evento.objects.get(titulo = nome_evento)
    return HttpResponse('A data do evento {} é {}'.format(nome_evento, objeto.data_evento))

def dataCriacao(request, nome_evento):
    objeto = Evento.objects.get(titulo = nome_evento)
    return HttpResponse('A data de criação do eveto {} é {}'.format(nome_evento, objeto.data_criacao))

def userEvento(request, nome_evento):
    objeto = Evento.objects.get(titulo = nome_evento)
    return HttpResponse('O user do evento {}  é {}'.format(nome_evento, objeto.usuario))