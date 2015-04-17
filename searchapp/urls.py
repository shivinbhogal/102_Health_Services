from django.conf.urls import patterns, url
from searchapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^speciality/(?P<speciality_type_slug>[\w\-]+)/$', views.speciality, name='speciality'),
	)