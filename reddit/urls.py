from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from posts.sitemaps import PostSitemap

sitemaps = {'posts': PostSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
