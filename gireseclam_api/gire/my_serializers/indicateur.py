from re import S
from rest_framework import serializers
from ..my_models.indicateur import IndicateurTb
from ..my_serializers.avancement_indicateur import AvancementIndicateurSerializer

#from ..models import Indicateur
class  IndicateurSerializer(serializers.ModelSerializer):
    avancement_indicateur = AvancementIndicateurSerializer(many=True , read_only=True)
    class Meta:
        model = IndicateurTb
        fields= ['indicateur_id','code','libelle','cible','valeur_base','valeur_representative','description','indicateur_resultat','sous_extrant','avancement_indicateur','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)