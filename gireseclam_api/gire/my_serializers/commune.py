from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import CommuneTb
from ..my_serializers.section_communale import SectionCommunaleSerializer
#from ..my_serializers.indicateur import IndicateurSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Commune
class  CommuneSerializer(serializers.ModelSerializer):  
    section_communale = SectionCommunaleSerializer(many=True , read_only=True)
    class Meta:
        model = CommuneTb
        fields= ['commune_id','libelle','departement','section_communale','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)