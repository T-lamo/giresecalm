from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import RisqueTb
from ..my_serializers.localite import LocaliteSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Risque
class  RisqueSerializer(serializers.ModelSerializer):   
    localite=LocaliteSerializer(many=True , read_only=True)
    class Meta:
       
        model = RisqueTb
        fields=['risque_id','libelle','localite','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)