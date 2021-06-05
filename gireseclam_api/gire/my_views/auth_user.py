from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
#from .models import AuthUser
from ..my_models.auth_user import AuthUser
#from .serializers import AuthUserSerializer
from ..my_serializers.auth_user import AuthUserSerializer
from django.http import Http404
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse("hello this is a test")

class AuthUserView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            users = AuthUser.objects.all()
            for u in users:
                print(u.fonction.libelle+" "+u.ong.nom)
                u.set_fonction_detail(u.fonction.libelle)
                u.set_ong_detail(u.ong.nom)
            serializer = AuthUserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            user= self.get_object(pk)
            serializer = AuthUserSerializer(user)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        user= self.get_object(pk)
        serializer = AuthUserSerializer(user)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            raise Http404