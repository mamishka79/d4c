from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
=======

# Create your models here.
>>>>>>> ebe27c2e35efd1f647ff36572ef3536834a6c4a7
