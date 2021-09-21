from typing import Optional
from django.db import models
from posts.models import Post
from django.shortcuts import get_object_or_404, render
from django.views import generic

from posts.models import Post


class PostListView(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'reddit/posts/list.html'


class PostDetailView(generic.DetailView):
    context_object_name = 'post'
    template_name = 'reddit/posts/detail.html'

    def get_object(self):
        post = get_object_or_404(Post,
                                 slug=self.kwargs['post'],
                                 publish__year=self.kwargs['year'],
                                 publish__month=self.kwargs['month'],
                                 publish__day=self.kwargs['day']
                                 )
        return post
