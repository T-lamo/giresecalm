from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import BassinVersantTb
from ..my_serializers.localite import LocaliteSerializer
#from ..my_serializers.indicateur import IndicateurSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import BassinVersant
class  BassinVersantSerializer(serializers.ModelSerializer):  
    localite = LocaliteSerializer(many=True , read_only=True)
 
    class Meta:
        model = BassinVersantTb
        fields= ['bassin_versant_id','libelle','section_communale','localite','statut']
       # fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)