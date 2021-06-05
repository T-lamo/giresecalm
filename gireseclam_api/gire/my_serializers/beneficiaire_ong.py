from re import S
from rest_framework import serializers
from ..my_models.ong import OngTb,BeneficiaireOngTb,BeneficiaireTb
from ..my_serializers.auth_user import AuthUserSerializer
class  BeneficiaireOngTbSerializer(serializers.ModelSerializer):
    users = AuthUserSerializer(many=True , read_only=True)
    class Meta:
        model = BeneficiaireOngTb
        fields= ['beneficiaire_id','ong_id','users']
        #fields='__all__'
    