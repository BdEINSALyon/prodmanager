from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from manager.docker import DockerClient


class ContainersView(LoginRequiredMixin, TemplateView):
    template_name = 'manager/containers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['containers'] = DockerClient().containers
        return context


class ContainerView(LoginRequiredMixin, TemplateView):
    template_name = 'manager/container.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['container'] = DockerClient().get_container(kwargs['id'])
        return context
