from django.shortcuts import get_object_or_404
from django.views import generic
from taggit.models import Tag

from posts.models import Post


class PostListView(generic.ListView):
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'reddit/posts/list.html'

    def get_queryset(self):
        if 'tag_slug' in self.kwargs:
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            return Post.objects.filter(tags__in=[tag])
        return Post.objects.all()


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
