from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from posts.models import Post


register = template.Library()


@register.simple_tag
def total_published_posts():
    return Post.published.count()


@register.inclusion_tag('reddit/tags/published_posts.html')
def published_posts(count=5):
    """Retrieve latest and most commented posts"""

    latest_posts = Post.published.order_by('-publish')[:count]
    most_commented = Post.published.annotate(total_comments=Count(
        'comments')).order_by('-total_comments')[:count]
    return {'latest_posts': latest_posts, 'most_commented': most_commented}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
