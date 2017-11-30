from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company/$', views.company, name='company'),
    url(r'^price/$', views.price, name='price'),
    url(r'^statement-entry/$', views.statement_entry, name='statement-entry'),
]