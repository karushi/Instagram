from django import forms
from .models import Image,Profile,Comment


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile_pics','Likes','Comments']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']        
        

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Comments',]