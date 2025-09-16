from django.db import models

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

    otp = models.CharField(max_length=200, null=True,blank=True)
    pass

# Create your models here.
# class User(models.Model):

#     title = models.CharField(max_length=200)
#     firstname = models.CharField(max_lenght=200)

#     # title = models.CharField(max_lenght=200)
#     description = models.TextField()
#     blog_image = models.ImageField(upload_to='blog_images/')
#     created_at = models.DateTimeField(auto_now_add=True)





class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=200)
    # first_name = models.CharField(max_lenght=200)

    # title = models.CharField(max_lenght=200)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title