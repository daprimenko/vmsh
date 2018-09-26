from django.conf.urls import url
from .views import Timetable, SubjectEdit, SubjectNew, SubjectDelete

urlpatterns = [
    url(r'^timetable$', Timetable.as_view(), name='timetable'),
    url(r'^timetable/subject/new/$', SubjectNew.as_view(), name='subject_new'),
    url(r'^timetable/subject/(?P<pk>\d+)/edit/$', SubjectEdit.as_view(), name='subject_edit'),
    url(r'^timetable/subject/(?P<pk>\d+)/delete/$', SubjectDelete.as_view(), name='subject_delete'),
]
