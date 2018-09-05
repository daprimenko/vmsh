from django.views.generic import ListView
from .models import Grade


class Timetable(ListView):
    model = Grade
    template_name = 'diary/timetable.html'
