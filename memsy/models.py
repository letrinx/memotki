from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mems(models.Model):
    title = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mem = models.ImageField(blank=False, upload_to='images/')

    def get_absolute_url(self):
        return "/mem/{}/".format(self.id)

