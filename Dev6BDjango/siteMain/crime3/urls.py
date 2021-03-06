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

"""url(r'^brink/$', include('crime3.urls'))"""
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^kind/?', views.kind, name="kind"),
    url(r'^woning/?', views.woning, name="woning"),
    url(r'^tankstation/?', views.tankstation, name="tankstation"),
    url(r'^brink/?', views.brink, name="brink"),
    url(r'^', views.index, name='indeXXX'),

]
