from django.shortcuts import render,get_object_or_404

from .models import ClientInfo
from .models import FournisseurInfo
from .models import ProduitInfo
from .models import EntreeInfo
from .models import SortieInfo
from .models import UtilisateurInfo


from datetime import date
today = date.today()


def login(request) :
	return render(request,'login.html')
def achats(request) :
	return render(request,'statistiques_achats.html')
def ventes(request) :
	return render(request,'statistiques_ventes.html')
def acceuil(request) :
	tous_produits = ProduitInfo.objects.all()
	return render(request,'acceuil.html',{'produits': tous_produits})
def gestion_clients(request) :
	tous_clients = ClientInfo.objects.all()
	return render(request,'gestion_clients.html', {'Clients': tous_clients})
def gestion_fournisseurs(request) :
	tous_fournisseurs = FournisseurInfo.objects.all()
	return render(request,'gestion_fournisseurs.html',{'fournisseurs': tous_fournisseurs})
def main(request) :
	return render(request,'statistiques.pbix')
def gestion_entree(request) :
	tous_entrees = EntreeInfo.objects.all()
	return render(request,'gestion_entree.html',{'entrees': tous_entrees})
def gestion_sortie(request) :
	tous_sorties = SortieInfo.objects.all()
	return render(request,'gestion_sortie.html',{'sorties': tous_sorties})
def gestion_produits(request) :
	tous_produits = ProduitInfo.objects.all()
	return render(request,'gestion_produits.html',{'produits': tous_produits})
def gestion_stock(request) :
	return render(request,'gestion_stock.html')
def administration(request) :
	return render(request,'administration.html')

def ajouter_client(request) :
	return render(request,'ajouter_client.html')
def ajouter_fournisseur(request) :
	return render(request,'ajouter_fournisseur.html')
def ajouter_produit(request) :
	return render(request,'ajouter_produit.html')
def ajouter_entree(request) :
	return render(request,'ajouter_entree.html')
def ajouter_sortie(request) :
	return render(request,'ajouter_sortie.html')

def ajouter_client_submit(request) :
	client_nom=request.POST["client_nom"]
	client_adresse=request.POST["client_adresse"]
	client_mail=request.POST["client_mail"]
	client_tel=request.POST["client_tel"]
	client_info = ClientInfo(client_nom=client_nom,client_tel=client_tel,client_mail=client_mail,client_adresse=client_adresse)
	client_info.save()
	return render(request,'ajouter_client.html')
def ajouter_fournisseur_submit(request) :
	fournisseur_nom=request.POST["fournisseur_nom"]
	fournisseur_adresse=request.POST["fournisseur_adresse"]
	fournisseur_mail=request.POST["fournisseur_mail"]
	fournisseur_tel=request.POST["fournisseur_tel"]
	fournisseur_info = FournisseurInfo(fournisseur_nom=fournisseur_nom,fournisseur_tel=fournisseur_tel,fournisseur_mail=fournisseur_mail,fournisseur_adresse=fournisseur_adresse)
	fournisseur_info.save()
	return render(request,'ajouter_fournisseur.html')
def ajouter_produit_submit(request) :
	produit_designation=request.POST["produit_designation"]
	produit_categorie=request.POST["produit_categorie"]
	produit_etat_stock=request.POST["produit_etat_stock"]
	produit_prix_achat=request.POST["produit_prix_achat"]
	produit_prix_vente=request.POST["produit_prix_vente"]
	fournisseur_info = ProduitInfo(produit_designation=produit_designation,produit_categorie=produit_categorie,produit_etat_stock=produit_etat_stock,produit_prix_achat=produit_prix_achat,produit_prix_vente=produit_prix_vente)
	fournisseur_info.save()
	return render(request,'ajouter_produit.html')
def ajouter_entree_submit(request) :
	entree_produit=request.POST["entree_produit"]
	entree_fournisseur=request.POST["entree_fournisseur"]
	entree_quantite=request.POST["entree_quantite"]
	obj = get_object_or_404(ProduitInfo,id=entree_produit)
	obj.produit_etat_stock=int(entree_quantite)+int(obj.produit_etat_stock)
	obj.save()
	entree_info = EntreeInfo(entree_produit=entree_produit,entree_fournisseur=entree_fournisseur,entree_quantite=entree_quantite,entree_date=today.strftime("%d/%m/%Y"))
	entree_info.save()
	return render(request,'ajouter_entree.html')
def ajouter_sortie_submit(request) :
	sortie_produit=request.POST["sortie_produit"]
	sortie_client=request.POST["sortie_client"]
	sortie_quantite=request.POST["sortie_quantite"]
	obj = get_object_or_404(ProduitInfo,id=sortie_produit)
	obj.produit_etat_stock=int(obj.produit_etat_stock)-int(sortie_quantite)
	obj.save()
	sortie_info = SortieInfo(sortie_produit=sortie_produit,sortie_fournisseur=sortie_client,sortie_quantite=sortie_quantite,sortie_date=today.strftime("%d/%m/%Y"))
	sortie_info.save()
	return render(request,'ajouter_sortie.html')

def verifier_connection(request) :
	username=request.POST["username"]
	password=request.POST["password"]
	obj = get_object_or_404(UtilisateurInfo,id=1)
	if obj.utilisateur_nom+" "+obj.utilisateur_prenom==username and obj.utilisateur_mdp==password :
		obj.utilisateur_dernier_cnx=today.strftime("%d/%m/%Y")
		obj.save()
		return render(request,'acceuil.html')
	else :
		return render(request,'login.html')

def supprimer_produit(request,produit_id) :
	obj = get_object_or_404(ProduitInfo,id=produit_id)
	obj.delete()
	return render(request,'gestion_produits.html')
def supprimer_fournisseur(request,fournisseur_id) :
	obj = get_object_or_404(FournisseurInfo,id=fournisseur_id)
	obj.delete()
	return render(request,'gestion_fournisseurs.html')
def supprimer_client(request,client_id) :
	obj = get_object_or_404(ClientInfo,id=client_id)
	obj.delete()
	return render(request,'gestion_clients.html')
def supprimer_entree(request,entree_id) :
	obj = get_object_or_404(EntreeInfo,id=entree_id)
	obj.delete()
	return render(request,'gestion_entree.html')
def supprimer_sortie(request,sortie_id) :
	obj = get_object_or_404(SortieInfo,id=sortie_id)
	obj.delete()
	return render(request,'gestion_sortie.html')


