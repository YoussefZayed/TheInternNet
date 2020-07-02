from django.db import models

# Create your models here.
class Contact(models.Model):
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField()

class Email(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    
