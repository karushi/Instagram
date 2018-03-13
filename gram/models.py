from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(max_length=150)
    photo = models.ImageField(upload_to='pics/',null=True, blank=True)
    user = models.ForeignKey(User)


    @classmethod
    def search_by_user(cls,search_term):    
        profile=cls.objects.filter(user__username__icontains=search_term)
        return profile  

    @classmethod
    def get_profile(cls):
            profile = Profile.objects.all()
            return profile
  

class Image(models.Model):
  image = models.ImageField(upload_to='image/', null=True, blank=True)
  image_name = models.CharField(max_length=25)
  Image_Caption = models.TextField(max_length=80)
  Likes = models.IntegerField(default=0)
  profile_pics = models.ForeignKey(Profile,on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  @classmethod
  def profile(cls):
      pass

  def delete_images(self):
      self.remove()    

  def save_images(self):
      self.save()      

  def update_caption(self, id):
      pass

  @classmethod
  def get_image_by_id(id):
      pass

  @classmethod
  def find_profile(self):
      profile = Profile.objects.all()
      return profile

class Comment(models.Model):
    Comments = models.CharField(max_length=70,blank=True,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    poster = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments', blank=True)

    def __str__(self):
        return self.Comments

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        return self.delete()