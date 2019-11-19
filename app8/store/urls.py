"""app8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from store import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('resultats', views.resultats, name='resultats'),
    url(r'^resultats(?P<page>\d+)$', views.resultats, name='resultats'),
    path('aliment', views.aliment, name='aliment'),
    path('aliment/<int:fav>/<int:prod>/<int:user>/', views.save_aliment, name='save_aliment')
]
