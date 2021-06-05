from gire.my_serializers.risque import RisqueSerializer
from gire.my_serializers.departement import DepartementSerializer
from gire.my_serializers.commune import CommuneSerializer
from gire.my_serializers.section_communale import SectionCommunaleSerializer
from gire.my_serializers.bassin_versant import BassinVersantSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
#from .models import OngTb
from ..my_models.espace_geographique import CommuneTb, DepartementTb, LocaliteTb, RisqueTb, SectionCommunaleTb
from ..my_models.espace_geographique import BassinVersantTb

#from .serializers import OngTbSerializer
from ..my_serializers.localite import LocaliteSerializer

class LocaliteView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = LocaliteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            localites = LocaliteTb.objects.all()
            serializer = LocaliteSerializer(localites, many=True)
            return Response(serializer.data)
        else:
            localite= self.get_object(pk)
            serializer = LocaliteSerializer(localite)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        localite= self.get_object(pk)
        serializer = LocaliteSerializer(localite)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return LocaliteTb.objects.get(pk=pk)
        except LocaliteTb.DoesNotExist:
            raise Http404

class BassinVersantView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = BassinVersantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            bassinVersants = BassinVersantTb.objects.all()
            serializer = BassinVersantSerializer(bassinVersants, many=True)
            return Response(serializer.data)
        else:
            bassinVersant= self.get_object(pk)
            serializer = BassinVersantSerializer(bassinVersant)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        bassinVersant= self.get_object(pk)
        serializer = BassinVersantSerializer(bassinVersant)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return BassinVersantTb.objects.get(pk=pk)
        except BassinVersantTb.DoesNotExist:
            raise Http404

class SectionCommunaleView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = SectionCommunaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            sectionCommunales = SectionCommunaleTb.objects.all()
            serializer = SectionCommunaleSerializer(sectionCommunales, many=True)
            return Response(serializer.data)
        else:
            sectionCommunale= self.get_object(pk)
            serializer = SectionCommunaleSerializer(sectionCommunale)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        sectionCommunale= self.get_object(pk)
        serializer = SectionCommunaleSerializer(sectionCommunale)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return SectionCommunaleTb.objects.get(pk=pk)
        except SectionCommunaleTb.DoesNotExist:
            raise Http404

class CommuneView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = CommuneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            communes = CommuneTb.objects.all()
            serializer = CommuneSerializer(communes, many=True)
            return Response(serializer.data)
        else:
            commune= self.get_object(pk)
            serializer = CommuneSerializer(commune)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        commune= self.get_object(pk)
        serializer = CommuneSerializer(commune)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return CommuneTb.objects.get(pk=pk)
        except CommuneTb.DoesNotExist:
            raise Http404


class DepartementView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = DepartementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            departements = DepartementTb.objects.all()
            serializer = DepartementSerializer(departements, many=True)
            return Response(serializer.data)
        else:
            departement= self.get_object(pk)
            serializer = DepartementSerializer(departement)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        departement= self.get_object(pk)
        serializer = DepartementSerializer(departement)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return DepartementTb.objects.get(pk=pk)
        except DepartementTb.DoesNotExist:
            raise Http404


class RisqueView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = RisqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            risques = RisqueTb.objects.all()
            serializer = RisqueSerializer(risques, many=True)
            return Response(serializer.data)
        else:
            risque= self.get_object(pk)
            serializer = RisqueSerializer(risque)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        risque= self.get_object(pk)
        serializer = RisqueSerializer(risque)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return RisqueTb.objects.get(pk=pk)
        except RisqueTb.DoesNotExist:
            raise Http404

