from django.conf.urls import patterns, include, url

urlpatterns = patterns('talksplanning.views',
    url(r'^/?$', 'home', name='home'),
    url(r'^b/(?P<id>\d+)/?$', 'batch_detail', name='batch_detail'),
)

