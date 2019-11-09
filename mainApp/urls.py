from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^education/(?P<pk>\d+)/$',
        #DetailView.as_view(model = Background, template_name ="mainApp/element.html")#
        views.element, name='element'),
    url(r'^education/$',
        #ListView.as_view(queryset = Background.objects.all(),template_name="mainApp/elements.html")#
        views.elements, name='elements'),
]
