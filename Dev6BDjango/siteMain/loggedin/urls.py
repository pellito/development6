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
    url(r'crime1/?', include('crime1.urls')),
    url(r'crime2/?', include('crime2.urls')),
    url(r'crime3/?', include('crime3.urls')),
    url(r'crime4/?', include('crime4.urls')),
    url(r'crime5/?', include('crime5.urls')),
    url(r'crime6/?', include('crime6.urls')),
    url(r'registercomplete/?', views.registercomplete, name='registercomplete'),


    url(r'^$', views.index, name='indexx')

]
