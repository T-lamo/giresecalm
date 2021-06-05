from re import S
from rest_framework import serializers
from ..my_models.indicateur import CategorieIndicateur
from ..my_serializers.extrant import ExtrantSerializer
from ..my_serializers.indicateur_resultat import IndicateurResultatSerializer

#from ..models import CategorieIndicateur
class  CategorieIndicateurSerializer(serializers.ModelSerializer):
    extrant = ExtrantSerializer(many=True , read_only=True)
    indicateur_resultat = IndicateurResultatSerializer(many=True , read_only=True)

    class Meta:
        model = CategorieIndicateur
       
        fields= ['categorie_indicateur_id','libelle','valeur_representative','extrant','indicateur_resultat','statut']
        #fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)