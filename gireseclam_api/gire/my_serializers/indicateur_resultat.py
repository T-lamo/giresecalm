from re import S
from rest_framework import serializers
from ..my_models.indicateur import IndicateurResultatTb
from ..my_serializers.auth_user import AuthUserSerializer
from ..my_serializers.indicateur import IndicateurSerializer 

#from ..models import IndicateurResultat
class  IndicateurResultatSerializer(serializers.ModelSerializer):
    indicateur = IndicateurSerializer(many=True , read_only=True)
    class Meta:
        model = IndicateurResultatTb
        fields= ['indicateur_resultat_id','code','libelle','valeur_representative','categorie_indicateur','indicateur','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)