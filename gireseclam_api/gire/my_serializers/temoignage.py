
from re import S
from rest_framework import serializers
from ..my_models.ong import OngTb,BeneficiaireOngTb,BeneficiaireTb,Temoignage
from ..my_serializers.auth_user import AuthUserSerializer
#from ..my_serializers.beneficiaire_ong import TemoignageOngTbSerializer
#from ..models import ong
class  TemoignageSerializer(serializers.ModelSerializer):
   # beneficiaire_ong = TemoignageOngTbSerializer(many=True , read_only=True)
    class Meta:
        model = Temoignage
        #fields= ['firstname','nom','beneficiaire_ong']
        fields='__all__'
