from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import LocaliteTb
from ..my_serializers.ong import BeneficiaireOngTbSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Localite
class  LocaliteSerializer(serializers.ModelSerializer):   
    beneficiaire=BeneficiaireOngTbSerializer(many=True , read_only=True)
    class Meta:
       
        model = LocaliteTb
        fields=['localite_id','libelle','bassin_versant','risque','beneficiaire','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)