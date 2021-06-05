from re import S
from rest_framework import serializers
from ..my_models.ong import OngTb,BeneficiaireOngTb,BeneficiaireTb
from ..my_serializers.auth_user import AuthUserSerializer
from ..my_serializers.beneficiaire import BeneficiaireTbSerializer
from ..my_serializers.beneficiaire_ong import BeneficiaireOngTbSerializer
from ..my_serializers.beneficiaire import BeneficiaireOngTbSerializer
from ..my_serializers.beneficiaire import BeneficiaireTbSerializer
from ..my_serializers.impact import ImpactSerializer
#from ..models import ong

class  OngTbSerializer(serializers.ModelSerializer):
    users = AuthUserSerializer(many=True , read_only=True)
    impact = ImpactSerializer(many=True , read_only=True)
    beneficiaire = BeneficiaireTbSerializer(many=True,read_only=True)

    class Meta:
        model = OngTb
        #fields= ['id','content','author','post']
        fields=['nom', 'users','beneficiaire','impact']
        extra_kwargs = {'beneficiaire': {'required': False}}
    def __str__(self):
        return '%s' % ( self.libelle)


