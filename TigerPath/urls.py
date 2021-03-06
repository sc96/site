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

app_name = 'site'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^fouryear/', include('fouryear.urls')),
    url(r'^$', views.home),
    url(r'^home$', views.home),
    #url(r'^user_profile/$', views.user_profile),
    url(r'^fouryear/(?P<search>$)', views.four_year),
    url(r'^fouryear/(?P<search>[A-Z]{3}$)', views.four_year, name='add'),
    url(r'^/fouryear/(?P<search>.*)/$', views.four_year, name='find'), #searchfunction
    url(r'^degreeprogress/$', views.degree_progress),
    #url(r'^princeton_course_approval/$', views.princeton_course_approval),
    #url(r'^outside_course_approval/$', views.outside_course_approval),
    url(r'^profile/$', views.profile),
    url(r'^about/$', views.about),
    url(r'^certificates/$', views.certificates),
    url(r'^aas/$', views.aas),
    url(r'^afs/$', views.afs),
    url(r'^ams/$', views.ams),
    url(r'^neu/$', views.neu),
    url(r'^mus/$', views.mus),
    url(r'^ghp/$', views.ghp),
    url(r'^fin/$', views.fin),
    url(r'^cwr/$', views.cwr),
    url(r'^urb/$', views.urb),
    url(r'^qcb/$', views.qcb),
    url(r'^gss/$', views.gss),
    url(r'^eas/$', views.eas),
    url(r'^rob/$', views.rob),
    url(r'^lin/$', views.lin),
    url(r'^vpl/$', views.vpl),
    url(r'^hel/$', views.hel),
    url(r'^lao/$', views.lao),
    url(r'^las/$', views.las),
    url(r'^dan/$', views.dan),
    url(r'^thr/$', views.thr),
    url(r'^vis/$', views.vis),
    url(r'^nes/$', views.nes),
    url(r'^egb/$', views.egb),
    url(r'^hum/$', views.hum),
    url(r'^lac/$', views.lac),
    url(r'^jud/$', views.jud),
    url(r'^apm/$', views.apm),
    url(r'^apc/$', views.apc),
    url(r'^env/$', views.env),
    url(r'^rus/$', views.rus),
    url(r'^sas/$', views.sas),
    url(r'^bio/$', views.bio),
    url(r'^arc/$', views.arc),
    url(r'^tic/$', views.tic),
    url(r'^tpp/$', views.tpp),
    url(r'^pse/$', views.pse),
    url(r'^eps/$', views.eps),
    url(r'^egr/$', views.egr),
    url(r'^phy/$', views.phy),
    url(r'^ecs/$', views.ecs),
    url(r'^geo/$', views.geo),
    url(r'^jaz/$', views.jaz),
    url(r'^med/$', views.med),
    url(r'^pla/$', views.pla),
    url(r'^mat/$', views.mat),
    url(r'^sml/$', views.sml),
    url(r'^tas/$', views.tas),
    url(r'^outsidecourseapproval/$', views.outside_course_approval),
    url(r'^cosdata/$', views.cos_data),
    url(r'^cosdatasemester/$', views.cos_data_semester),
    url(r'^cosdatacourse/$', views.cos_data_course),
    url(r'^cosdatareq/$', views.cos_data_req),
   # url(r'^princetoncourseapproval/$', views.princeton_course_approval),
    url(r'^schedulesharing/$', views.schedule_sharing),
    url(r'^share/(?P<shared_user>[-\w]+)/$', views.share),
    #url(r'^home/degreeprogress/$', views.degree_progress),
    # CAS. No changes needed for the other urls.
    url(r'^login$', cas.views.login, name='login'),
    url(r'^logout$', cas.views.logout, name='logout'),
   # url(r'^.*', views.notFound)
]
