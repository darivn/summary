from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from background.models import Background

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset = Background.objects.all(),
        template_name="Background/elements.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Background, template_name ="background/element.html"))
]
