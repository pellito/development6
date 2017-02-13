"""siteMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^1', views.snoep, name='snoep'),
    url(r'^2', views.redbull, name='redbull'),
    url(r'^3', views.telefoon, name='telefoon'),
    url(r'^4', views.klanten_telefoon, name='klanten_telefoon'),
    url(r'^5', views.drugs, name='drugs'),
    url(r'^6', views.container, name='container'),

    url(r'^', views.index, name='index')

]
