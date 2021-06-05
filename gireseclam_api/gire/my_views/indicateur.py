

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
#from .models import OngTb
from ..my_models.ong import OngTb,BeneficiaireTb
from ..my_models.indicateur import CategorieIndicateur,ExtrantTb,IndicateurResultatTb,SousExtrantTb,IndicateurTb,AvancementIndicateurTb
#from .serializers import OngTbSerializer
from ..my_serializers.ong import OngTbSerializer
from ..my_serializers.beneficiaire import BeneficiaireTbSerializer
from ..my_serializers.categorie_indicateur import CategorieIndicateurSerializer
from ..my_serializers.extrant import ExtrantSerializer
from ..my_serializers.indicateur_resultat import IndicateurResultatSerializer
from ..my_serializers.sous_extrant import SousExtrantSerializer
from ..my_serializers.indicateur import IndicateurSerializer
from ..my_serializers.avancement_indicateur import AvancementIndicateurSerializer
from django.http import Http404
from rest_framework import status

class CategorieIndicateurView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = CategorieIndicateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            categorieIndicateurs = CategorieIndicateur.objects.all()
            serializer = CategorieIndicateurSerializer(categorieIndicateurs, many=True)
            return Response(serializer.data)
        else:
            categorieIndicateur= self.get_object(pk)
            serializer = CategorieIndicateurSerializer(categorieIndicateur)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        categorieIndicateur= self.get_object(pk)
        serializer = CategorieIndicateurSerializer(categorieIndicateur)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return CategorieIndicateur.objects.get(pk=pk)
        except CategorieIndicateur.DoesNotExist:
            raise Http404

class ExtrantView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = ExtrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            extrants = ExtrantTb.objects.all()
            serializer = ExtrantSerializer(extrants, many=True)
            return Response(serializer.data)
        else:
            extrant= self.get_object(pk)
            serializer = ExtrantSerializer(extrant)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        extrant= self.get_object(pk)
        serializer = ExtrantSerializer(extrant)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return ExtrantTb.objects.get(pk=pk)
        except ExtrantTb.DoesNotExist:
            raise Http404

class IndicateurResultatView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = IndicateurResultatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            indicateurResultats = IndicateurResultatTb.objects.all()
            serializer = IndicateurResultatSerializer(indicateurResultats, many=True)
            return Response(serializer.data)
        else:
            indicateurResultat= self.get_object(pk)
            serializer = IndicateurResultatSerializer(indicateurResultat)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        indicateurResultat= self.get_object(pk)
        serializer = IndicateurResultatSerializer(indicateurResultat)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return IndicateurResultatTb.objects.get(pk=pk)
        except IndicateurResultatTb.DoesNotExist:
            raise Http404

class SousExtrantView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = SousExtrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            sousExtrants = SousExtrantTb.objects.all()
            serializer = SousExtrantSerializer(sousExtrants, many=True)
            return Response(serializer.data)
        else:
            sousExtrant= self.get_object(pk)
            serializer = SousExtrantSerializer(sousExtrant)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        sousExtrant= self.get_object(pk)
        serializer = SousExtrantSerializer(sousExtrant)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return SousExtrantTb.objects.get(pk=pk)
        except SousExtrantTb.DoesNotExist:
            raise Http404

class IndicateurView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = IndicateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            indicateurs = IndicateurTb.objects.all()
            serializer = IndicateurSerializer(indicateurs, many=True)
            return Response(serializer.data)
        else:
            indicateur= self.get_object(pk)
            serializer = IndicateurSerializer(indicateur)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        indicateur= self.get_object(pk)
        serializer = IndicateurSerializer(indicateur)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return IndicateurTb.objects.get(pk=pk)
        except IndicateurTb.DoesNotExist:
            raise Http404
class AvancementIndicateurView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = AvancementIndicateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            avancementIndicateurs = AvancementIndicateurTb.objects.all()
            serializer = AvancementIndicateurSerializer(avancementIndicateurs, many=True)
            return Response(serializer.data)
        else:
            avancementIndicateur= self.get_object(pk)
            serializer = AvancementIndicateurSerializer(avancementIndicateur)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        avancementIndicateur= self.get_object(pk)
        serializer = AvancementIndicateurSerializer(avancementIndicateur)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return AvancementIndicateurTb.objects.get(pk=pk)
        except AvancementIndicateurTb.DoesNotExist:
            raise Http404
