"""TigerPath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from . import views
import cas.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^fouryear/', include('fouryear.urls')),
    url(r'^$', views.home),
    #url(r'^user_profile/$', views.user_profile),
    url(r'^fouryear/$', views.four_year, name='Your Plan'),
    url(r'^degreeprogress/$', views.degree_progress),
    url(r'^princeton_course_approval/$', views.princeton_course_approval),
    url(r'^outside_course_approval/$', views.outside_course_approval),
    url(r'^profile/$', views.profile),
    #url(r'^home/degreeprogress/$', views.degree_progress),
    # CAS. No changes needed for the other urls.
    url(r'^login$', cas.views.login, name='login'),
    url(r'^logout$', cas.views.logout, name='logout'),
]
