
# Create your views here.

from django.shortcuts import render

from .models import Post

# all_posts = [
#     { 'slug': 'hiking-tips', 'title': 'Mountain Hiking Tips', 'excerpt': 'Discover essential tips for a safe and enjoyable mountain hiking experience.', 'date': '2024-01-15', 'image': 'mountains.jpg', 'content': 'Remember to always inform someone about your hiking plans and estimated return time. Happy hiking!' },
#     { 'slug': 'city-guide', 'title': 'City Travel Guide', 'excerpt': 'Explore the best attractions, dining, and accommodations in top cities around the world.', 'date': '2024-02-10', 'image': 'woods.jpg', 'content': 'When visiting a new city, consider using public transportation to get around efficiently and experience local life.' },
#     { 'slug': 'beach-vacation', 'title': 'Beach Vacation Ideas', 'excerpt': 'Find out about the most beautiful beaches and activities for your next beach vacation.', 'date': '2024-03-05', 'image': 'coding.jpg', 'content': 'Discover the best beaches and activities for your next beach vacation.' },
# ]

all_posts = Post.objects.all();


def get_date(post):
    return post.date

def index(request):
    latest_posts = all_posts.order_by('-date')
    print(latest_posts)
    return render(request, 'blog/index.html', {'posts': latest_posts})

def posts(request):
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    return render(request, 'blog/all-posts.html', {'posts': sorted_posts})

def post_detail(request, slug):
    latest_posts = all_posts.order_by('-date')
    post = next((post for post in latest_posts if post.slug == slug), None)
    return render(request, 'blog/post-details.html', {'post': post})