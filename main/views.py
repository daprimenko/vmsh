from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutPost
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_posts'] = AboutPost.objects.all()
        return context
