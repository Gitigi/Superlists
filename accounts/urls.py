from django.conf.urls import patterns,url
from accounts import views

urlpatterns = patterns('',
                       url(r'^login$',views.persona_login,name='persona_login'),
                       )
