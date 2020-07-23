from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#owner = models.ForeignKey(User, on_delete=models.CASCADE)
class Posting(models.Model):
    title= models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)

class SavedPosting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dateApplied = models.DateField(auto_now_add=True)
    template = models.ForeignKey(Posting, on_delete=models.CASCADE)

class UserSaved(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
