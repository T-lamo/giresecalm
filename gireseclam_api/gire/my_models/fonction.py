from django.db import models

class FonctionTb(models.Model):
    fonction_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fonction_tb'