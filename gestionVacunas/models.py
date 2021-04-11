from django.db import models

# Create your models here.

class Vacunado(models.Model):
    nombre=models.CharField(max_length=80)
    email=models.EmailField(blank=True, null=True)