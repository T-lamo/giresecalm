from re import S
from rest_framework import serializers
from ..my_models.indicateur import SousExtrantTb
from ..my_serializers.indicateur import IndicateurSerializer
#from ..models import SousExtrant
class  SousExtrantSerializer(serializers.ModelSerializer):
    indicateur = IndicateurSerializer(many=True , read_only=True)
    class Meta:
        model = SousExtrantTb
        fields= ['sous_extrant_id','code','libelle','valeur_representative','extrant','indicateur','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)