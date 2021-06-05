from django.db import models
from .espace_geographique import LocaliteTb

class OngTb(models.Model):
    ong_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    statut = models.IntegerField()
    #beneficiaire = models.ManyToManyField('BeneficiaireTb', related_name='beneficiaire', blank=True)


    class Meta:
        managed = False
        db_table = 'ong_tb'

class BeneficiaireOngTb(models.Model):
    beneficiaire_ong_id = models.AutoField(primary_key=True)
    beneficiaire = models.ForeignKey('BeneficiaireTb', models.DO_NOTHING,related_name='beneficiaire_ong')
    ong = models.ForeignKey('OngTb', models.DO_NOTHING, related_name='ong_beneficiaire')

    class Meta:
        managed = False
        db_table = 'beneficiaire_ong_tb'


class BeneficiaireTb(models.Model):
    beneficiaire_id = models.AutoField(primary_key=True)
    localite = models.ForeignKey('LocaliteTb', models.DO_NOTHING, related_name='beneficiaire')
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    cin = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=10)
    statut = models.IntegerField()
    ong = models.ManyToManyField('OngTb', related_name='beneficiaire', blank=True)


    class Meta:
        managed = False
        db_table = 'beneficiaire_tb'

class Temoignage(models.Model):
    temoignage_id = models.AutoField(primary_key=True)
    beneficiaire = models.ForeignKey(BeneficiaireTb, models.DO_NOTHING,related_name='temoignage')
    contenu = models.CharField(max_length=255)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temoignage'

class ImpactTb(models.Model):
    impact_id = models.AutoField(primary_key=True)
    type_impact = models.ForeignKey('TypeImpactTb', models.DO_NOTHING,related_name='impact')
    ong = models.ForeignKey('OngTb', models.DO_NOTHING, related_name='impact')
    libelle = models.CharField(max_length=255)
    type = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'impact_tb'

class TypeImpactTb(models.Model):
    type_impact_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_impact_tb'







