from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    image_pics = Image.objects.all()
    return render(request,'index.html',{"image_pics":image_pics})
