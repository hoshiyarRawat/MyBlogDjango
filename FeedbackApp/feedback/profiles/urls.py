from django.urls import path


from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all/", views.ListProfilesView.as_view(), name="profile_list"),

]