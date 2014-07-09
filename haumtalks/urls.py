from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# to name index
import talksplanning.views

urlpatterns = patterns('',
    url(r'^/?$', talksplanning.views.home, name="index"),
    url(r'^', include('talksplanning.urls', namespace="talksplanning")),

    url(r'^admin/', include(admin.site.urls)),
)
