from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  bio = models.TextField(max_length=150)
  photo = models.ImageField(upload_to='pics/',null=True, blank=True)
  user = models.ForeignKey(User)
  

class Image(models.Model):
  image = models.ImageField(upload_to='image/', null=True, blank=True)
  image_name = models.CharField(max_length=25)
  Image_Caption = models.TextField(max_length=80)
  Likes = models.IntegerField(default=0)
  profile_pics = models.ForeignKey(Profile)
  user = models.ForeignKey(User)
  Comments = models.CharField(max_length=140)


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
  
  def find_profile(self):
      pass

  @classmethod
  def search_by_user(cls,search_term):
        
        images=cls.objects.filter(image_icontains=search_term)
        return images   
    



  
