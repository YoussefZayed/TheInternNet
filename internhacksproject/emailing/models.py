from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Template(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    
class EmailSent(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=200)
    dateCreated = models.DateField(auto_now_add=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)