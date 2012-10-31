from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.views import index, olamundo, parametros, lista, novo, artigo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapps.views.home', name='home'),
    # url(r'^djangoapps/', include('djangoapps.foo.urls')),
    url(r'^$', index),
    url(r'^artigos/$', lista),
    url(r'^artigo/(?P<id_artigo>\d+)/$', artigo),
    url(r'^novo/$', novo),
    url(r'^olamundo/$', olamundo),
    url(r'^parametros/(\d{1,3})/$', parametros),

    # Uncomment the admin/doc line below to enable admin documentation:

    # url(r'^$', 'djangoapps.views.generic.date_based.archive_index', {
    #     'queryset': Artigo.objects.all(),
    #     'date_field': 'publicacao'
    #     }),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
