from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Define your URL patterns here
    #path('book/<int:book_id>/', views.book_details, name='book_details'),

    path('book/<slug:slug>/', views.book_details, name='book_details'),

]
