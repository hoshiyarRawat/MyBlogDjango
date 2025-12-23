from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import BookOutlet

# Create your views here.
def index(request):
    books = BookOutlet.objects.all()

    return render(request, 'book_outlet/index.html', {
        'books': books
    })

def book_details(request, slug):
    # try:
    #     book = BookOutlet.objects.get(id=book_id)
    # except BookOutlet.DoesNotExist:
    #     raise Http404("Book does not exist")
    #     book = None

    book = get_object_or_404(BookOutlet, slug=slug)

    return render(request, 'book_outlet/book_details.html', {
        'book': book
    })