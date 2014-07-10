from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('eventsplanning.views',
    url(r'^/?$', 'home', name='home'),
    url(r'^b/(?P<id>\d+)/?$', 'event_detail', name='event_detail'),
    url(r'^b/(?P<event_id>\d+)/inscription$', 'event_form', name='event_form'),
    url(r'^b/(?P<event_id>\d+)/proposal$', 'talk_form', name='talk_form'),
)

