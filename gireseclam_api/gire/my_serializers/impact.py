from re import S
from rest_framework import serializers
from ..my_models.ong import ImpactTb
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Impact
class  ImpactSerializer(serializers.ModelSerializer):
    
   # sousextrant = SousExtrantSerializer(many=True , read_only=True)
    class Meta:
        model = ImpactTb
        #fields= ['extrant_id','code','libelle','valeur_representative','statut','sousextrant','categorie_indicateur']
        fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)