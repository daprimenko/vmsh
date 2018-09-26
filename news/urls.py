from django.conf.urls import url
from . import views
from .views import NewsView, PostDetailView, PostNew, PostEdit, PostDelete

urlpatterns = [
    url(r'^news$', NewsView.as_view(), name='news_page'),
    url(r'^news/post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^news/post/(?P<pk>\d+)/edit/$', PostEdit.as_view(), name='post_edit'),
    url(r'^news/post/new/$', PostNew.as_view(), name='post_new'),
    url(r'^news/post/(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post_delete'),
]