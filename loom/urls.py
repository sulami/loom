from django.conf.urls import patterns, include, url
from django.contrib import admin

from campaigns import urls, views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/campaigns/', views.campaign_overview,
        name='account_campaigns'),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'', include(urls, namespace='campaigns')),
)

