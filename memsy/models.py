from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mems(models.Model):
    title = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mem = models.ImageField(blank=False, upload_to='images/')

    def get_absolute_url(self):
        return "/mem/{}/".format(self.id)

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    mem = models.ForeignKey(Mems, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)


