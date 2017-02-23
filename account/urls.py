"""accounts URL configuration
"""
from django.conf.urls import url
from django.views.generic.base import TemplateView

from account import views

urlpatterns = [
    url(r'^oauth/(?P<provider>[a-z_]*)/callback', views.OAuthCallback.as_view(), name='oauth_callback'),
    url(r'^oauth/(?P<provider>[a-z_]*)/login', views.OAuthLogin.as_view(),  name='oauth_login'),
    url(r'^$', TemplateView.as_view(template_name='account/login.html'), name='home')
]
