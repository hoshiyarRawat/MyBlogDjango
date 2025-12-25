from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"

class ListProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"

# def store_file(file):
#     with open("temp/"+str(file)+"", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {'form': form})

#     def post(self, request):
#         print('---checking files---', str(request.FILES["image"]))
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = UserProfile(image=request.FILES["image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles/")
#         print(request.FILES)
#         print('---checking files---')
#         return render(request, "profiles/create_profile.html", {'form': form})