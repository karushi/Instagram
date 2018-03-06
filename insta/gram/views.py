from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Image,Profile

# Create your views here.
 
@login_required(login_url='/accounts/login/')
def welcome(request):
    title = 'Instagram'
    image_pics = Image.objects.all()
    return render(request,'index.html',{"title":title,"image_pics":image_pics})



@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'Insta'
    profile = Profile.objects.all()
    return render(request,'profile/profile.html',{"title":title, "profile":profile})  

  