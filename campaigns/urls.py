from django.conf.urls import patterns, include, url

from campaigns import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cid>\d+)/$', views.campaign, name='campaign'),
    url(r'^(?P<eid>\d+)/save/$', views.save_event, name='save_event'),
)

