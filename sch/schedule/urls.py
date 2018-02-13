from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.batch_home, name='batch_home'),
]