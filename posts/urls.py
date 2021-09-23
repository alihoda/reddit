from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='tag_post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.PostDetailView.as_view(), name='post_detail'),
]
