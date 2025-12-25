
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView

from django.views.generic import CreateView

from .models import Review



# Create your views here.

class ReviewView(CreateView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class ReviewView(View):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/thank-you'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, 'reviews/review.html', {'form': form})

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request, 'reviews/review.html', {'form': form})


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66



    # def review(request):
    #     if request.method == 'POST':
    #         form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect('/thank-you')

    #     else:
    #         form = ReviewForm()

    #     return render(request, 'reviews/review.html', {'form': form})

    #return render(request, 'reviews/review.html')

# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you for your feedback!'
        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_queryset = super().get_queryset()
    #     data = base_queryset.filter(rating__gte=3)
    #     return data


class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'
    model = Review



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs.get('id')
    #     context['review'] = Review.objects.get(id=review_id)
    #     return context