from django.conf.urls import url
from .views import Timetable

urlpatterns = [
    url(r'^timetable$', Timetable.as_view(), name='timetable'),
]
