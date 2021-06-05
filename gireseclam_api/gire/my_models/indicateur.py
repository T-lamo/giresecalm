from django.db import models

class AvancementIndicateurTb(models.Model):
    avancement_indicateur_id = models.AutoField(primary_key=True)
    indicateur = models.ForeignKey('IndicateurTb', models.DO_NOTHING,related_name="avancement_indicateur")
    realisation = models.FloatField()
    annee = models.DateField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'avancement_indicateur_tb'

class CategorieIndicateur(models.Model):
    categorie_indicateur_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorie_indicateur'

class ExtrantTb(models.Model):
    extrant_id = models.AutoField(primary_key=True)
    categorie_indicateur = models.ForeignKey(CategorieIndicateur, models.DO_NOTHING,related_name='extrant')
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'extrant_tb'

class IndicateurOngTb(models.Model):
    indicateur_ong_id = models.AutoField(primary_key=True)
    indicateur = models.ForeignKey('IndicateurTb', models.DO_NOTHING)
    ong = models.ForeignKey('OngTb', models.DO_NOTHING)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_ong_tb'


class IndicateurResultatTb(models.Model):
    indicateur_resultat_id = models.AutoField(primary_key=True)
    categorie_indicateur = models.ForeignKey(CategorieIndicateur, models.DO_NOTHING,related_name='indicateur_resultat')
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_resultat_tb'


class IndicateurTb(models.Model):
    indicateur_id = models.AutoField(primary_key=True)
    indicateur_resultat = models.ForeignKey(IndicateurResultatTb, models.DO_NOTHING, blank=True, null=True,related_name='indicateur')
    sous_extrant = models.ForeignKey('SousExtrantTb', models.DO_NOTHING, blank=True, null=True,related_name='indicateur')
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    cible = models.FloatField()
    valeur_base = models.FloatField()
    valeur_representative = models.FloatField()
    description = models.CharField(max_length=1000)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_tb'
class SousExtrantTb(models.Model):
    sous_extrant_id = models.AutoField(primary_key=True)
    extrant = models.ForeignKey(ExtrantTb, models.DO_NOTHING,related_name='sousextrant')
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sous_extrant_tb'