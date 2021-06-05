from django.test import TestCase
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Beneficiaire
from .serializers import BeneficiaireSerializer
# Create your tests here.

class BeneficiaireView(APIView):
    def get (self,request, format=None):
        beneficiaires = Beneficiaire.objects.all()
        serializer = BeneficiaireSerializer(beneficiaires, many=True)
        return Response(serializer.data)

