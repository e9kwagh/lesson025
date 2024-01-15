from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15,  blank=True)
    email = models.EmailField(max_length=15,  blank=True)
    address = models.CharField(max_length=100,blank=True)
    phoneNumber = models.CharField(max_length=10)
    linkedin = models.CharField(max_length=50,  blank=True)
    facebook = models.CharField(max_length=50,  blank=True)
    twitter = models.CharField(max_length=50,  blank=True)


    # class Meta:
    #     ordering = ["updated", "created"]

    def __str__(self):
        return self.user.username
