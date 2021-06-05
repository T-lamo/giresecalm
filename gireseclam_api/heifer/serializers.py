from re import S
from rest_framework import serializers
from .models import Beneficiaire
from .models import Comment,Post


class  BeneficiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiaire
        fields= ['name','sexe']

class  CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields= ['id','content','author','post']
    def __str__(self):
        return '%d: %s' % (self.id, self.title)

class  PostSerializer(serializers.ModelSerializer):
    post_ob = CommentSerializer(many=True , read_only=True)

    class Meta:
        model = Post
        fields= ['id' ,'title','content','author','post_ob']

    