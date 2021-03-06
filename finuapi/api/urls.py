from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company/$', views.company, name='company'),
    url(r'^price/$', views.price, name='price'),
    url(r'^reported-entry/$', views.reported_entry, name='reported-entry'),
    url(r'^all-companies/$', views.all_companies, name='all-companies'),
    url(r'^company-rates/$', views.company_rates, name='company-rates'),
]