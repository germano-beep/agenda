"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('evento/local/<str:nome_evento>/', views.localEvento),
    path('evento/descricao/<str:nome_evento>/', views.descricaoEvento),
    path('evento/data_evento/<str:nome_evento>/', views.dataEvento),
    path('evento/data_criacao/<str:nome_evento>/', views.dataCriacao),
    path('evento/user/<str:nome_evento>/', views.userEvento),

    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/'))
    # path('', views.index)


]
