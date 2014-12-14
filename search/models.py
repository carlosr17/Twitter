from django.db import models

# Create your models here.

class Palabra(models.Model):
	nombre=models.CharField(max_length=100)
	time= models.DateTimeField(auto_now=True)