from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(\d+)$', views.weather),
    url(r'find$', views.get_city_id, name='find'),
]
