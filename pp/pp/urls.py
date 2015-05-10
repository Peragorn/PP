from django.conf.urls import patterns, include, url
from django.contrib import admin

from wnioski.views import WniosekDetailView, Przedmiot_ZamowieniaDetailView

from wnioski import views

urlpatterns = patterns('',
    # Examples:

	url(r'^$', 'wnioski.views.home', name='home'),
	url(r'^login/$', 'wnioski.views.user_login', name='user_login'),
	url(r'^signup/$', 'wnioski.views.register', name='register'),
	url(r'^search/$', 'wnioski.views.search', name='search'),
	url(r'^firma/(?P<slug>[-_\w]+)/$', Przedmiot_ZamowieniaDetailView.as_view(), name='firma_detail'),
	url(r'^wniosek/(?P<slug>[-_\w]+)/$', WniosekDetailView.as_view(), name='wniosek_detail'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
