from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^news$', views.news_page, name='news_page'),
    url(r'^news/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^about$', views.about, name='about'),
    url(r'^timetable$', views.timetable, name='timetable'),
]