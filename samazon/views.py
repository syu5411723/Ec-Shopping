from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post


class Home(TemplateView):
    template_name = 'samazon/home.html'


class PostList(ListView):
    model = Post
    template_name = 'samazon/list.html'

    def get_queryset(self):
        queryset = Post.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains=qs)

        return queryset


class PostDetail(DetailView):
    model = Post
    template_name = 'samazon/detail.html'
