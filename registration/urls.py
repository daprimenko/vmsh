from django.conf.urls import include, url
from django.contrib.auth import views
from .views import ProfileView, LoginView, LogoutView

urlpatterns = [
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^accounts/login/$', LoginView.as_view(template_name='registration/login_required.html'), name='login_required'),
    url(r'^logout\?next=(?P<next>[\w/]+)$', LogoutView.as_view(), name='logout'),
    url('^', include('django.contrib.auth.urls')),
]