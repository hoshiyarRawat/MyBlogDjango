from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='submit_review'),
    path('thank-you', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:id>', views.SingleReviewView.as_view(), name='single_review'),
]
