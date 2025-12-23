from . import views
from django.urls import path


urlpatterns = [
    # Your URL patterns here
    path("", views.index, name="start-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]