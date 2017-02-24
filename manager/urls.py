"""accounts URL configuration
"""
from django.conf.urls import url

from manager import views

urlpatterns = [
    url(r'^containers', views.ContainersView.as_view(), name='manager_containers'),
    url(r'^container/(?P<id>[a-z0-9]*)', views.ContainerView.as_view(),  name='manager_container')
]
