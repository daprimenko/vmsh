from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Grade, Subject
from django.core.urlresolvers import reverse_lazy


class Timetable(ListView):
    model = Grade
    template_name = 'diary/timetable.html'


class SubjectEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'diary.change_subject'
    model = Subject
    fields = ['grade', 'name', 'day', 'room', 'time']
    template_name = 'diary/subject_edit.html'
    success_url = reverse_lazy('timetable')

    def get_context_data(self, **kwargs):
        context = super(SubjectEdit, self).get_context_data(**kwargs)
        context['form_title'] = 'Редактирование предмета'
        context['page_title'] = 'Редактирование'
        return context


class SubjectNew(PermissionRequiredMixin, CreateView):
    permission_required = 'diary.add_subject'
    model = Subject
    fields = ['grade', 'name', 'day', 'room', 'time']
    template_name = 'diary/subject_edit.html'
    success_url = reverse_lazy('timetable')

    def get_context_data(self, **kwargs):
        context = super(SubjectNew, self).get_context_data(**kwargs)
        context['form_title'] = 'Добавление предмета'
        context['page_title'] = 'Новый предмет'
        return context


class SubjectDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'diary.delete_subject'
    model = Subject
    template_name = 'diary/subject_confirm_delete.html'
    success_url = reverse_lazy('timetable')
    context_object_name = 'subject'
