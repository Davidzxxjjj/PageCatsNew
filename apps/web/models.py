from django.db import models

# Create your models here.

class Cats(models.Model):
    pk_Cats = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, blank=False, null=False)
    Raza = models.CharField(max_length=50, blank=False, null=False)
    Color = models.TextField(blank=False, null=True)
    Edad = models.TextField(blank=False, null=True)