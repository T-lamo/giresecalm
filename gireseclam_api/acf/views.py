from django.shortcuts import render
import requests
import logging
from django.http import HttpResponse

# Create your views here.
from django.http import JsonResponse
from requests.api import request
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class OwnApiView(APIView):
    
     def get (self,request, format=None):
        r = requests.get('http://127.0.0.1:8000/beneficiaire/7')
        if r.status_code == requests.codes.ok:
        #  print(r.headers['content-type'])
            commit_data = r.json()
        logger = logging.getLogger(__name__)
        logger.error("Testing")
        print(commit_data)
        #serializer = BeneficiaireSerializer(beneficiaires, many=True)
        #return Response({'status':200})
        return Response(commit_data[0])

