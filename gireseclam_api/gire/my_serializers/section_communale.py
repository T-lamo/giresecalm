from re import S
from rest_framework import serializers
from ..my_models.espace_geographique import SectionCommunaleTb
from ..my_serializers.bassin_versant import BassinVersantSerializer
#from ..my_serializers.indicateur import IndicateurSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import SectionCommunale
class  SectionCommunaleSerializer(serializers.ModelSerializer):  
    bassin_versant = BassinVersantSerializer(many=True , read_only=True)
 
    class Meta:
        model = SectionCommunaleTb
        fields= ['section_communale_id','libelle','commune','bassin_versant','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)