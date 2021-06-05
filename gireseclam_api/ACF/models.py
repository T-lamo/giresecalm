from django.db import models

# Create your models here.
class Beneficiaire(models.Model):
    name = models.CharField(max_length=200)
    sexe= models.CharField(max_length=200)

    def __str__(self):
        return self.name