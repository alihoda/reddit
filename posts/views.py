from django.db.models import Count
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

    def get_context_data(self, **kwargs):
        post_obj = self.get_object()
        post_tags_id = post_obj.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(
            tags__in=post_tags_id).exclude(id=post_obj.id)
        similar_posts = similar_posts.annotate(same_tags=Count(
            'tags')).order_by('-same_tags', '-publish')[:4]

        context = super().get_context_data(**kwargs)
        context['similar_posts'] = similar_posts
        return context
