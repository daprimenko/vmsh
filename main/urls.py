from django.conf.urls import url
from django.views.generic import RedirectView, TemplateView
from .views import AboutView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='news_page'), name='main'),
    url(r'^about$', AboutView.as_view(), name='about'),
]