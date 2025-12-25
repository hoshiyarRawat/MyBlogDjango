from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all/", views.ListProfilesView.as_view(), name="profile_list"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
