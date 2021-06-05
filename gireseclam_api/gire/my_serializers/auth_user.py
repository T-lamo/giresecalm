from re import S
from rest_framework import serializers
from ..my_models.auth_user import AuthUser
from ..my_models.fonction import FonctionTb
#from ..my_serializers.fonction import FonctionTbSerializer
#from ..models import AuthUser
class  AuthUserSerializer(serializers.ModelSerializer):
    #fonction_id = FonctionTbSerializer(many=True , read_only=True)
   # libelle_fonction=serializers.RelatedField(source='fonction_id', read_only=True)
    class Meta:
        model = AuthUser
        fields= ['username','password','first_name','last_name','email','telephone','is_staff','is_active','date_joined','is_superuser','fonction_detail','ong_detail']
        #fields='__all__'


    def __str__(self):
        return '%d: %s' % (self.username, self.first_name)