from django.conf.urls import patterns, include, url

from campaigns import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cid>\d+)/$', views.campaign, name='campaign'),
    url(r'^(?P<eid>\d+)/save/$', views.save_event, name='save_event'),
    url(r'^(?P<cid>\d+)/(?P<sid>\d+)/new/$', views.new_event, name='new_event'),
    url(r'^(?P<eid>\d+)/del/$', views.delete_event, name='delete_event'),
    url(r'^(?P<cid>\d+)/notes/$', views.notes, name='notes'),
)

