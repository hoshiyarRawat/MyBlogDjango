from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="My Name",max_length=100, min_length=4, error_messages={
#         'required': 'Please enter your name',
#         'min_length': 'Name must be at least 4 characters long',
#         'max_length': 'Name cannot exceed 10 characters'
#     })

#     revfiew_text = forms.CharField(label="Your Feedback",widget=forms.Textarea, max_length=500, min_length=10, error_messages={
#         'required': 'Please enter your review',
#         'min_length': 'Review must be at least 10 characters long',
#         'max_length': 'Review cannot exceed 500 characters'
#     })

#     rating = forms.IntegerField(label="Rating (1-5)", min_value=1, max_value=5, error_messages={
#         'required': 'Please provide a rating between 1 and 5',
#         'min_value': 'Rating must be at least 1',
#         'max_value': 'Rating cannot exceed 5'
#     })
    #email = forms.EmailField()
    #review = forms.CharField(widget=forms.Textarea)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        labels = {
            'user_name': 'My Name',
            'review_text': 'Your Feedback',
            'rating': 'Rating (1-5)'
        }