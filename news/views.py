from django.utils import timezone

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import Post


class NewsView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'


class PostNew(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    model = Post
    fields = ['title', 'text']
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('news_page', urlconf='news.urls')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostNew, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostNew, self).get_context_data(**kwargs)
        context['form_title'] = 'Добавление новости'
        context['page_title'] = 'Новая запись'
        return context


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    model = Post
    fields = ['title', 'text']
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('news_page', urlconf='news.urls')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostEdit, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostEdit, self).get_context_data(**kwargs)
        context['form_title'] = 'Редактирование новости'
        context['page_title'] = 'Редактирование'
        return context


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    model = Post
    success_url = reverse_lazy('news_page')
    template_name = 'news/post_confirm_delete.html'

