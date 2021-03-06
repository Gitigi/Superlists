from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import views
from lists import urls as list_urls
from accounts import urls as accounts_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.home_page,name='home'),
    url(r'^lists/',include(list_urls)),
    url(r'^accounts/',include(accounts_urls)),
)
