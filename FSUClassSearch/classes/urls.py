from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'classes'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^view$', views.view, name="view")
]

urlpatterns += staticfiles_urlpatterns()