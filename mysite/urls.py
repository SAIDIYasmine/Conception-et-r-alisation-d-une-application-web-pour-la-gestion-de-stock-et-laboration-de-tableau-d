"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include

urlpatterns = [
    path('', views.login),
    path('acceuil/', views.acceuil),
    path('gestion_clients/', views.gestion_clients),
    path('gestion_fournisseurs/', views.gestion_fournisseurs),
    path('gestion_produits/', views.gestion_produits),
    path('gestion_entree/', views.gestion_entree),
    path('gestion_sortie/', views.gestion_sortie),
    path('gestion_stock/', views.gestion_stock),
    path('administration/', views.administration),
    path('statistiques_achats/', views.achats),
    path('statistiques_ventes/', views.ventes),
    path('admin/',admin.site.urls),
    path('main/', views.main),

    path('ajouter_client/', views.ajouter_client),
    path('ajouter_fournisseur/', views.ajouter_fournisseur),
    path('ajouter_produit/', views.ajouter_produit),
    path('ajouter_entree/', views.ajouter_entree),
    path('ajouter_sortie/', views.ajouter_sortie),
    path('supprimer_produit/<int:produit_id>/', views.supprimer_produit),
    path('supprimer_fournisseur/<int:fournisseur_id>/', views.supprimer_fournisseur),
    path('supprimer_client/<int:client_id>/', views.supprimer_client),
    path('supprimer_entree/<int:entree_id>/', views.supprimer_entree),
    path('supprimer_sortie/<int:sortie_id>/', views.supprimer_sortie),

    path('ajouter_client_submit/', views.ajouter_client_submit),
    path('ajouter_fournisseur_submit/', views.ajouter_fournisseur_submit),
    path('ajouter_produit_submit/', views.ajouter_produit_submit),
    path('ajouter_entree_submit/', views.ajouter_entree_submit),
    path('ajouter_sortie_submit/', views.ajouter_sortie_submit),

    path('verifier_connection/', views.verifier_connection),


    path('accounts/', include('django.contrib.auth.urls')), # new

]
urlpatterns+=staticfiles_urlpatterns()