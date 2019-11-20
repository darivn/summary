from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^experience/$', views.experience, name='experience'),
    url(r'^education/(?P<pk>\d+)/$', views.element, name='element'),
    url(r'^education/$', views.elements, name='elements'),
]
