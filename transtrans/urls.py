from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list_detail import object_list
from sections.models import Section

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', object_list,  {'queryset': Section.objects.all(), 'template_name': 'index.html'} ,name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)
