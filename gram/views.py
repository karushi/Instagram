from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .form import EditProfileForm,UploadForm,CommentsForm
from .models import Image,Profile,Comment

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

@login_required(login_url="/accounts/login/")
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"username":searched_name})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


@login_required(login_url="/accounts/login/")
def upload(request):
    title = 'Insta'
    current_user = request.user
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = current_user
                    upload.profile_pics = profile
                    upload.save()
                    return redirect('index')
            else:
                form = UploadForm()
            return render(request,'upload.html',{"title":title, "user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def comment(request, id):
    title = 'Instagrum |Comment'
    post = get_object_or_404(Image, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.poster = post
            comment.save()
            return redirect('index')
    else:
        form = CommentsForm()
        
    return render(request,'comments.html',{"title":title,"form":form})