from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # El ID que viene por default el ORM
    detail = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    publish_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.id)


class Comment(models.Model):
    detail = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

""" class Friendly(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE) """
