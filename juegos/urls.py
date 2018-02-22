from django.conf.urls import url
from juegos import views
from demo import settings

urlpatterns = [
    url(r'^list/$', views.noticia_list, name='noticia_list'),
    url(r'^edit/(?P<pk>\d+)$', views.noticia_update, name='noticia_edit'),
]