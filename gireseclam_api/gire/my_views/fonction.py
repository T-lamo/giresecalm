from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
#from .models import FonctionTb
from ..my_models.fonction import FonctionTb
#from .serializers import FonctionTbSerializer
from ..my_serializers.fonction import FonctionTbSerializer
from django.http import Http404
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse("hello this is a test")

class FonctionTbView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = FonctionTbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            users = FonctionTb.objects.all()
            serializer = FonctionTbSerializer(users, many=True)
            return Response(serializer.data)
        else:
            user= self.get_object(pk)
            serializer = FonctionTbSerializer(user)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        user= self.get_object(pk)
        serializer = FonctionTbSerializer(user)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return FonctionTb.objects.get(pk=pk)
        except FonctionTb.DoesNotExist:
            raise Http404