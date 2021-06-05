from re import S
from rest_framework import serializers
from ..my_models.indicateur import AvancementIndicateurTb
#from ..my_serializers.indicateur import IndicateurSerializer
#from ..my_serializers.sous_extrant import SousExtrantSerializer

#from ..models import AvancementIndicateur
class  AvancementIndicateurSerializer(serializers.ModelSerializer):
    #indicateur = IndicateurSerializer(many=True , read_only=True)
   
    class Meta:
        model = AvancementIndicateurTb
        #fields= ['avancement_indicateur_id','annee','indicateur','statut']
        fields='__all__'
    def __str__(self):
        return '%s' % ( self.libelle)