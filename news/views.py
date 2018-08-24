from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post


def main(request):
    return redirect('news_page')


def news_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})


def about(request):
    return render(request, 'news/about.html', {})


def timetable(request):
    return render(request, 'news/timetable.html', {})