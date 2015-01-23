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
    url(r'^save_note/(?P<nid>\d+)/$', views.save_note, name='save_note'),
    url(r'^del_note/(?P<nid>\d+)/$', views.delete_note, name='delete_note'),
    url(r'^new_note/(?P<cid>\d+)/$', views.new_note, name='new_note'),
)

