"""avec_amour_vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
#from . import views
from .views import criar_pedido, cadastrar_item, lista_itens

#app_name = 'avec_amour_vendas'

urlpatterns = [
    path('', criar_pedido, name='home'),  # Redireciona para "criar pedido"
    path('criar-pedido/', criar_pedido, name='criar_pedido'),
    path('cadastrar-item/', cadastrar_item, name='cadastrar_item'),
    path('lista-itens/', lista_itens, name='lista_itens'),  # Rota para listar itens

]
