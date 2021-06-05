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
from .models import Beneficiaire, Comment, Post
from .serializers import BeneficiaireSerializer,CommentSerializer,PostSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from django.contrib.auth.models import User

# Create your tests here.

class BeneficiaireView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = BeneficiaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_object(self, pk):
        try:
            return Beneficiaire.objects.get(pk=pk)
        except Beneficiaire.DoesNotExist:
            raise Http404

   

    def put(self, request, pk, format=None):
        beneficiaire = self.get_object(pk)
        serializer = BeneficiaireSerializer(beneficiaire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        beneficiaire = self.get_object(pk)
        beneficiaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get (self,request, format=None):
        beneficiaires = Beneficiaire.objects.all()
        serializer = BeneficiaireSerializer(beneficiaires, many=True)
        return Response(serializer.data)

    def get(self, request, pk=-1, format=None):
        if pk ==-1:
            beneficiaires = Beneficiaire.objects.all()
            serializer = BeneficiaireSerializer(beneficiaires, many=True)
            return Response(serializer.data)
        elif pk == 7:
            r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
            #if r.status_code == requests.codes.ok:
            #  print(r.headers['content-type'])
            commit_data = r.json()
            logger = logging.getLogger(__name__)
            logger.error("Testing")
            logger.error(commit_data)
            return Response(commit_data.keys())
        else:

            beneficiaire = self.get_object(pk)
            serializer = BeneficiaireSerializer(beneficiaire)
            return Response(serializer.data)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username':user.username,
            'firstname':user.first_name,
            'lastname':user.last_name,
            'email': user.email
        })
class ProfilView(APIView):
   
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
   

    def post (self, request, *args, **kwargs):
        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        #user.first_name = request.data['firstname']
        #user.last_name = request.data['lastname']
        user.save()
        return Response({'status':200})

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def set_name(self, name):
  	self.name = name
    
  def get_name(self):
  	return self.name
    
  def set_ecole(self, ecole):
  	self.ecole =ecole
  
  def get_ecole(self):
  	return self.ecole

class Ecole:
  def __init__(self, name, lieu):
    self.name = name
    self.lieu = lieu

p1 = Person("John", 36)
p2 = Person("Carlie",32)

commit_data=[]
#r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
#r= requests.get('http://127.0.0.1:8000/apiview')
#if r.status_code == requests.codes.ok:
        #  print(r.headers['content-type'])
  #  commit_data = r.json()

persons = [p1,p2]
x=1
for p in persons:
  if x ==1 :
    p.set_ecole(Ecole("ACF", "Leogane"))
  else :
    p.set_ecole(Ecole("ACF", "Leogane"))
  x=2
    
  
  #print(p.name)
  #print(p.ecole.lieu)
print(persons[0].ecole)
print(persons[0].name+" "+persons[0].ecole.lieu+" "+persons[0].ecole.name)
print(persons[1].name+" "+persons[1].ecole.lieu+" "+persons[1].ecole.name)

  
  
  
  
ecole = Ecole("ESIH", "Nazon")
p1.set_ecole(ecole)

#print(p1.ecole.lieu)


#print(p1.name)
#print(p1.age)

p1.set_name("James")

#print(p1.name)

# Python program showing a use
# of get() and set() method in
# normal function

class CallApiView(APIView):
     def __init__(self):
         pass
     def get (self,request, format=None):
        r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
        if r.status_code == requests.codes.ok:
        #  print(r.headers['content-type'])
            commit_data = r.json()
        logger = logging.getLogger(__name__)
        logger.error("Testing")
        print(commit_data.keys())
        #serializer = BeneficiaireSerializer(beneficiaires, many=True)
        #return Response({'status':200})
        return Response(commit_data.keys())

     def getImage(self):
        x = np.arange(0, 2 * np.pi, 0.01)
        s = np.cos(x) ** 2
        plt.plot(x, s)
 
        plt.xlabel('xlabel(X)')
        plt.ylabel('ylabel(Y)')
        plt.title('Simple Graph!')
        plt.grid(True)
 
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

     def getData(request):
        samp = np.random.randint(100, 600, size=(4, 5))
        print(samp)
        df = pd.DataFrame(samp, index=['avi', 'dani', 'rina', 'dina'],
                          columns=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        return HttpResponse(df.to_html(classes='table table-bordered')) 

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
        #return Response({'status':200})apiview
        return Response(commit_data[0])
class CommentView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1, format=None):
        if pk==-1:
            comments = Comment.objects.all()
            for c in comments:
                print(c.post.post_ob)
                print(c.post.post_ob.author)

                print(c.post.author)


                #c.set_post_ob(Response(CommentSerializer(c.post).data))
                #print(c.get_post)
            #comments = Comment.objects.select_related('post').all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        else:
            p = self.get_object(pk)
            serializer = CommentSerializer(p)
            return Response(serializer.data)

    def getUnique (self,pk): 
        p = self.get_object(pk)
        serializer = CommentSerializer(p)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404



class PostView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post (self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get (self,request, pk=-1 , format=None): 
        if pk==-1:
            Posts = Post.objects.all()
            serializer = PostSerializer(Posts, many=True)
            return Response(serializer.data)
        else:
            p = self.get_object(pk)
            serializer = PostSerializer(p)
            return Response(serializer.data)
    
    def getUnique (self,pk): 
        p = self.get_object(pk)
        serializer = PostSerializer(p)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404