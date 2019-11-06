from django.conf.urls import url, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
