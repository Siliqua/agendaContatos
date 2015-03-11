from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agendaContatos.views.home', name='home'),
    # url(r'^agendaContatos/', include('agendaContatos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url para imagens
    url(r'^admin/agenda(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),


        (r'^$', 'agenda.views.index'),
    url(
        r'^agenda/view/(?P<nome>[^\.]+).html',
        'agenda.views.view_contato',
        name='view_contato'),
)
