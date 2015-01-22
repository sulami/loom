from django.conf.urls import patterns, include, url

from campaigns import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cid>\d+)/$', views.campaign, name='campaign'),
    url(r'^(?P<cid>\d+)/notes/$', views.notes, name='notes'),
    url(r'^save_event/(?P<eid>\d+)/$', views.save_event, name='save_event'),
    url(r'^new_event/(?P<cid>\d+)/(?P<sid>\d+)/$', views.new_event,
        name='new_event'),
    url(r'^del_event/(?P<eid>\d+)/$', views.delete_event, name='delete_event'),
    url(r'^note/(?P<nid>\d+)/$', views.note, name='note'),
)

