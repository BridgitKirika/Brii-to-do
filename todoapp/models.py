from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.urls import reverse
from django.db.models.signals import post_save

from PIL import Image

from django.urls import reverse


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('index')

    
    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/default.jpg', upload_to='media/')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


    # img = Image.open(self.image.path)
        
    # if img.height  > 300 or img.width > 300:
    #     output_size = (300,300)
    #     img.thumbnail(output_size)
    #     img.save(self.image.path)