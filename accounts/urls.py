from django.conf.urls import patterns,url
from accounts import views

urlpatterns = patterns('',
                       url(r'^login$',views.persona_login,name='persona_login'),
                       url(r'^logout$','django.contrib.auth.views.logout',{'next_page':'/'},name='logout'),
                       )
