from django.conf.urls import patterns, include, url
from django.contrib import admin

from wnioski.views import WniosekDetailView, Przedmiot_ZamowieniaDetailView

from wnioski import views

urlpatterns = patterns('',
    # Examples:

	url(r'^$', 'wnioski.views.home', name='home'),
	
	url(r'^login/$', 'wnioski.views.user_login', name='user_login'),
	url(r'^logout/$', 'wnioski.views.user_logout', name='user_logout'),
	url(r'^register/$', 'wnioski.views.register', name='register'),
	
	url(r'^about/$', 'wnioski.views.about', name='about'),
	url(r'^contact/$', 'wnioski.views.contact', name='contact'),

	url(r'^wniosek/my/$', 'wnioski.views.wniosek_moje', name='wniosek_moje'),
	url(r'^wniosek/new/$', 'wnioski.views.wniosek_new', name='wniosek_new'),
	url(r'^wniosek/example/$', 'wnioski.views.example', name='example'),
	
	url(r'^wniosek/przedmiot/$', 'wnioski.views.przedmiot_zamowienia', name='przedmiot_zamowienia'),

	url(r'^wniosek/dzial_nauki/$', 'wnioski.views.wniosek_dzial_nauki', name='wniosek_dzial_nauki'),

	url(r'^wniosek/(?P<mymodel_id>[-_\w]+)/$', 'wnioski.views.my_model_view', name='wniosek_detail'),
	url(r'^wniosek/view/(?P<mymodel_id>[-_\w]+)/$', 'wnioski.views.my_model_view', name='wniosek_detail'),
	url(r'^firma/(?P<slug>[-_\w]+)/$', Przedmiot_ZamowieniaDetailView.as_view(), name='firma_detail'),
	
	# url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
