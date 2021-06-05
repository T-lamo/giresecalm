from gire.my_serializers.section_communale import SectionCommunaleSerializer
from django.urls import path
from django.urls.resolvers import URLPattern
#from .views import AuthUserView
from .my_views.auth_user import AuthUserView
from .my_views.fonction import FonctionTbView
from .my_views.ong import ImpactView, OngTbView,BeneficiaireOngTbView,BeneficiaireTbView, TemoignageView, TypeImpactView
from .my_views.indicateur import CategorieIndicateurView,ExtrantView,IndicateurResultatView,SousExtrantView,IndicateurView,AvancementIndicateurView
from .my_views.espace_geographique import BassinVersantView, CommuneView, DepartementView, LocaliteView, RisqueView, SectionCommunaleView

urlpatterns=[
    #path('',views.index, name='index'),
    path('user/<int:pk>', AuthUserView.as_view() , name='authuser'),
    path('user', AuthUserView.as_view() , name='authuser'),
    path('fonction', FonctionTbView.as_view() , name='authuser'),
    path('fonction/<int:pk>', FonctionTbView.as_view() , name='authuser'),
    path('ong/<int:pk>', OngTbView.as_view() , name='ong'),
    path('ong', OngTbView.as_view() , name='ong'),
    path('beneficiaire/<int:pk>', BeneficiaireTbView.as_view() , name='beneficiaire'),
    path('beneficiaire', BeneficiaireTbView.as_view() , name='ong'),
    path('beneficiaireong/<int:pk>', BeneficiaireOngTbView.as_view() , name='bong'),
    path('beneficiaireong', BeneficiaireOngTbView.as_view() , name='bong'),
    path('categorieindicateur/<int:pk>', CategorieIndicateurView.as_view() , name='categorieindicateur'),
    path('categorieindicateur', CategorieIndicateurView.as_view() , name='categorieindicateur'),
    path('extrant/<int:pk>', ExtrantView.as_view() , name='extrant'),
    path('extrant', ExtrantView.as_view() , name='extrant'),
    path('sousextrant/<int:pk>', SousExtrantView.as_view() , name='sousextrant'),
    path('sousextrant', SousExtrantView.as_view() , name='sousextrant'),
    path('indicateurresultat/<int:pk>', IndicateurResultatView.as_view() , name='indicateurresultat'),
    path('indicateurresultat', IndicateurResultatView.as_view() , name='indicateurresultat'),
    path('indicateur/<int:pk>', IndicateurView.as_view() , name='indicateur'),
    path('indicateur', IndicateurView.as_view() , name='indicateur'),
    path('avancementindicateur/<int:pk>', AvancementIndicateurView.as_view() , name='avancementindicateur'),
    path('avancementindicateur', AvancementIndicateurView.as_view() , name='avancementindicateur'),
    path('localite/<int:pk>', LocaliteView.as_view() , name='localite'),
    path('localite', LocaliteView.as_view() , name='localite'),
    path('bassinversant/<int:pk>', BassinVersantView.as_view() , name='bassinversant'),
    path('bassinversant', BassinVersantView.as_view() , name='bassinversant'),
    path('sectioncommunale/<int:pk>', SectionCommunaleView.as_view() , name='sectioncommunale'),
    path('sectioncommunale', SectionCommunaleView.as_view() , name='sectioncommunale'),
    path('commune/<int:pk>', CommuneView.as_view() , name='commune'),
    path('commune', CommuneView.as_view() , name='commune'),
    path('departement/<int:pk>', DepartementView.as_view() , name='departement'),
    path('departement', DepartementView.as_view() , name='departement'),
    path('temoignage/<int:pk>', TemoignageView.as_view() , name='temoignage'),
    path('temoignage', TemoignageView.as_view() , name='temoignage'),
    path('risque/<int:pk>', RisqueView.as_view() , name='risque'),
    path('risque', RisqueView.as_view() , name='risque'),
    path('impact/<int:pk>', ImpactView.as_view() , name='impact'),
    path('impact', ImpactView.as_view() , name='impact'),
    path('typeimpact/<int:pk>', TypeImpactView.as_view() , name='typeimpact'),
    path('typeimpact', TypeImpactView.as_view() , name='typeimpact'),
]