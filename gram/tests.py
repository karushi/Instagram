from django.test import TestCase
from .models import Profile, Image
# Create your tests here.
class ImageTestClass(TestCase):
     
    def setUp(self):
         self.image=Image(image='image',image_name="landscape",image_caption="beautiful",likes="100",imgae=karush)


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save(self):
        self.imgae.save_imgaes()
        imgae=imgae.objects.all()
        self.assertTrue(len(imgaes)>0)  

    def test_delete(self):
        self.image.save_images()
        images=Image.objects.all()
        self.image.delete_images()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)    