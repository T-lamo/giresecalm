import re
from django.db import models


class BassinVersantTb(models.Model):
    bassin_versant_id = models.IntegerField(primary_key=True)
    section_communale = models.ForeignKey('SectionCommunaleTb', models.DO_NOTHING,related_name='bassin_versant')
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bassin_versant_tb'

class CommuneTb(models.Model):
    commune_id = models.AutoField(primary_key=True)
    departement = models.ForeignKey('DepartementTb', models.DO_NOTHING,related_name='commune')
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commune_tb'


class DepartementTb(models.Model):
    departement_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departement_tb'

class LocaliteTb(models.Model):
    localite_id = models.AutoField(primary_key=True)
    bassin_versant = models.ForeignKey(BassinVersantTb, models.DO_NOTHING, blank=True, null=True, related_name='localite')
    risque = models.ForeignKey('RisqueTb', models.DO_NOTHING,related_name='localite')
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'localite_tb'

class SectionCommunaleTb(models.Model):
    section_communale_id = models.AutoField(primary_key=True)
    commune = models.ForeignKey(CommuneTb, models.DO_NOTHING,related_name='section_communale')
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'section_communale_tb'
        
class RisqueTb(models.Model):
    risque_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'risque_tb'