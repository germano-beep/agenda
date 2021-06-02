from django.http import request
from core.models import Evento
from django.shortcuts import redirect, render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
   return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
    

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect ('/')
        else: 
            messages.error(request,"Usuário ou senha inválido")

    return  redirect('/')
    
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados) 

@login_required(login_url='/login/')
def evento(request):
    return render(request,'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        local = request.POST.get('local')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                             local=local,
                             data_evento=data_evento,
                             descricao=descricao,
                             usuario=usuario)

    return redirect('/')
    
       


# def localEvento(request, nome_evento):
#     objeto = Evento.objects.get(titulo = nome_evento)
#     return HttpResponse('O local do evento {} será em {}'.format(nome_evento, objeto.local))

# def descricaoEvento(request, nome_evento):
#     objeto = Evento.objects.get(titulo = nome_evento)
#     return HttpResponse('A descricacao do evento {} é {}'. format(nome_evento, objeto.descricao))

# def dataEvento(request, nome_evento):
#     objeto = Evento.objects.get(titulo = nome_evento)
#     return HttpResponse('A data do evento {} é {}'.format(nome_evento, objeto.data_evento))

# def dataCriacao(request, nome_evento):
#     objeto = Evento.objects.get(titulo = nome_evento)
#     return HttpResponse('A data de criação do eveto {} é {}'.format(nome_evento, objeto.data_criacao))

# def userEvento(request, nome_evento):
#     objeto = Evento.objects.get(titulo = nome_evento)
#     return HttpResponse('O user do evento {}  é {}'.format(nome_evento, objeto.usuario))

# def index(request):
#     return redirect('/agenda/')

