from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import DepartementTb
from ..my_serializers.commune import CommuneSerializer
#from ..my_serializers.indicateur import IndicateurSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Departement
class  DepartementSerializer(serializers.ModelSerializer):  
    commune = CommuneSerializer(many=True , read_only=True)
    class Meta:
        
        model = DepartementTb
        fields= ['departement_id','libelle','commune','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)