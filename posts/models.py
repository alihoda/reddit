from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    body = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    objects = models.Manager()
    published = PublishManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])