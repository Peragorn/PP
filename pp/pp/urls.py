from django.conf.urls import patterns, include, url
from django.contrib import admin

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
	
	url(r'^przedmiot/new/$', 'wnioski.views.przedmiot_new', name='wniosek_new'),
	url(r'^przedmiot/(?P<mymodel_id>[-_\w]+)/$', 'wnioski.views.przedmiot_podglad', name='przedmiot_podglad'),

	
	url(r'^wniosek/dzial_nauki/$', 'wnioski.views.wniosek_dzial_nauki', name='wniosek_dzial_nauki'),

	url(r'^wniosek/(?P<mymodel_id>[-_\w]+)/$', 'wnioski.views.my_model_view', name='wniosek_detail'),
	url(r'^wniosek/view/(?P<mymodel_id>[-_\w]+)/$', 'wnioski.views.wniosek_podglad', name='wniosek_detail'),

	url(r'^admin/', include(admin.site.urls)),
)
