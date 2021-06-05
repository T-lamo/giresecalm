from re import S
from rest_framework import serializers
from ..my_models.fonction import FonctionTb
from ..my_serializers.auth_user import AuthUserSerializer

#from ..models import Fonction
class  FonctionTbSerializer(serializers.ModelSerializer):
    users = AuthUserSerializer(many=True , read_only=True)

    class Meta:
        model = FonctionTb
        #fields= ['id','content','author','post']
        fields=['libelle', 'users']
    def __str__(self):
        return '%s' % ( self.libelle)