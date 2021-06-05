from re import S
from rest_framework import serializers
from ..my_models.ong import TypeImpactTb
from ..my_serializers.impact import ImpactSerializer

#from ..models import TypeImpact
class  TypeImpactSerializer(serializers.ModelSerializer):
    
    impact = ImpactSerializer(many=True , read_only=True)
    class Meta:
        model = TypeImpactTb 
        fields= ['type_impact_id','libelle','impact','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)