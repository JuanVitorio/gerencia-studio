"""
URL configuration for gerencia_studio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from anotacoes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', clientes, name = 'clientes'),
    path('new_anotacao/', nova_anotacao, name = 'new_anotacao' ),
    path('update_anotacao/<int:pk>', update_anotacao, name = 'update_anotacao'),
    path('delete_anotacao/<int:pk>', delete_anotacao, name = 'delete_anotacao' ),
    path('cliente_detalhe/<int:pk>', lista_detalhes, name = 'cliente_detalhe'),
]
