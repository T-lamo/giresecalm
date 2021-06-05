from re import S
from rest_framework import serializers
from .models import AuthUser



class  AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        #fields= ['id','content','author','post']
        fields='__all__'
    def __str__(self):
        return '%d: %s' % (self.username, self.first_name)

