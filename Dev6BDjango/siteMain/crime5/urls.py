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
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^1/?', views.offroad,name='offroad'),
    url(r'^2/?', views.binnenstad,name='binnenstad'),
    url(r'^3/?', views.platteland,name='platteland'),
    url(r'^4/?', views.snelweg,name='snelweg'),
    url(r'^', views.index, name='index')
]
