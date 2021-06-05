from gire.my_serializers.type_impact import TypeImpactSerializer
from gire.my_serializers.impact import ImpactSerializer
from gire.my_serializers.temoignage import TemoignageSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
#from .models import OngTb
from ..my_models.ong import ImpactTb, OngTb,BeneficiaireTb,BeneficiaireOngTb, Temoignage, TypeImpactTb
#from .serializers import OngTbSerializer
from ..my_serializers.ong import OngTbSerializer,BeneficiaireOngTbSerializer
from ..my_serializers.beneficiaire import BeneficiaireTbSerializer
from ..my_serializers.beneficiaire_ong import BeneficiaireOngTbSerializer
from django.http import Http404
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse("hello this is a test")

class OngTbView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = OngTbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            ongs = OngTb.objects.all()
            for ong in ongs:
                print(ong.ong_beneficiaire)

                
            print("good")
            serializer = OngTbSerializer(ongs, many=True)
            return Response(serializer.data)
        else:
            ong= self.get_object(pk)
            serializer = OngTbSerializer(ong)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        ong= self.get_object(pk)
        serializer = OngTbSerializer(ong)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return OngTb.objects.get(pk=pk)
        except OngTb.DoesNotExist:
            raise Http404

class BeneficiaireTbView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = BeneficiaireTbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            beneficiaires = BeneficiaireTb.objects.all()
            serializer = BeneficiaireTbSerializer(beneficiaires, many=True)
            return Response(serializer.data)
        else:
            beneficiaire= self.get_object(pk)
            serializer = BeneficiaireTbSerializer(beneficiaire)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        beneficiaire= self.get_object(pk)
        serializer = BeneficiaireTbSerializer(beneficiaire)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return BeneficiaireTb.objects.get(pk=pk)
        except BeneficiaireTb.DoesNotExist:
            raise Http404

class TemoignageView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = TemoignageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            temoignages = Temoignage.objects.all()
            serializer = TemoignageSerializer(temoignages, many=True)
            return Response(serializer.data)
        else:
            temoignage= self.get_object(pk)
            serializer = TemoignageSerializer(temoignage)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        temoignage= self.get_object(pk)
        serializer = TemoignageSerializer(temoignage)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Temoignage.objects.get(pk=pk)
        except Temoignage.DoesNotExist:
            raise Http404


class BeneficiaireOngTbView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = BeneficiaireOngTbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            beneficiaireOngs = BeneficiaireOngTb.objects.all()
            serializer = BeneficiaireOngTbSerializer(beneficiaireOngs, many=True)
            return Response(serializer.data)
        else:
            beneficiaireOng= self.get_object(pk)
            serializer = BeneficiaireOngTbSerializer(beneficiaireOng)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        beneficiaireOng= self.get_object(pk)
        serializer = BeneficiaireOngTbSerializer(beneficiaireOng)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return BeneficiaireOngTb.objects.get(pk=pk)
        except BeneficiaireOngTb.DoesNotExist:
            raise Http404

class ImpactView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = ImpactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            impacts = ImpactTb.objects.all()
            serializer = ImpactSerializer(impacts, many=True)
            return Response(serializer.data)
        else:
            impact= self.get_object(pk)
            serializer = ImpactSerializer(impact)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        impact= self.get_object(pk)
        serializer = ImpactSerializer(impact)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return ImpactTb.objects.get(pk=pk)
        except ImpactTb.DoesNotExist:
            raise Http404


class TypeImpactView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = TypeImpactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            typeImpacts = TypeImpactTb.objects.all()
            serializer = TypeImpactSerializer(typeImpacts, many=True)
            return Response(serializer.data)
        else:
            typeImpact= self.get_object(pk)
            serializer = TypeImpactSerializer(typeImpact)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        typeImpact= self.get_object(pk)
        serializer = TypeImpactSerializer(typeImpact)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return TypeImpactSerializer.objects.get(pk=pk)
        except TypeImpactTb.DoesNotExist:
            raise Http404

