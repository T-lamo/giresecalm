"""gireseclam_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from heifer.views import ProfilView, CallApiView, CommentView, PostView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from heifer.views import BeneficiaireView,CustomAuthToken, ProfilView, OwnApiView
from gire.views import index
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from acf import views 
from django.urls import include,path


admin.site.site_header = "HEIFER Admin"
admin.site.site_title = "HEIFER Admin Portal"
admin.site.index_title = "Welcome to Heifer Interface"


urlpatterns = [
    path('', BeneficiaireView.as_view(), name='beneficiaire'),
    path('admin/', admin.site.urls),
    path('beneficiaire/<int:pk>', BeneficiaireView.as_view(), name='getbeneficiaire'),
    path('beneficiaire/', BeneficiaireView.as_view(), name='beneficiaire'),
    #path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('profile/', ProfilView.as_view()),
    path('apiview/', CallApiView.getImage, name='apiview'),
    path('ownapi/', OwnApiView.as_view(), name='apiview'),
    path('post/', PostView.as_view(), name='postview'),
    path('post/<int:pk>', PostView.as_view() , name='postviewunique'),
    path('comment/', CommentView.as_view(), name='commentview'),
    path('comment/<int:pk>', CommentView.as_view(), name='getcomment'),
    #gire beginroute

    path('giresec/', index),
    path('gire/', include('gire.urls'))



    



   # path('mbeneficiaire/<int:pk>', BeneficiaireView.as_view(), name='beneficiaire'),
   # path('uniquebeneficiaire/<int:pk>', BeneficiaireView.as_view(), name='beneficiaire'),

]
