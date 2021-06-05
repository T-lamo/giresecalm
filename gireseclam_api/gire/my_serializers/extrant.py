from re import S
from rest_framework import serializers
from ..my_models.indicateur import ExtrantTb
from ..my_serializers.auth_user import AuthUserSerializer
from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import Extrant
class  ExtrantSerializer(serializers.ModelSerializer):
    
    sousextrant = SousExtrantSerializer(many=True , read_only=True)
    class Meta:
        model = ExtrantTb
        fields= ['extrant_id','code','libelle','valeur_representative','statut','sousextrant','categorie_indicateur']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)