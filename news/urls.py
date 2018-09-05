from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news$', views.news_page, name='news_page'),
    url(r'^news/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^news/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^news/post/new/$', views.post_new, name='post_new'),
]