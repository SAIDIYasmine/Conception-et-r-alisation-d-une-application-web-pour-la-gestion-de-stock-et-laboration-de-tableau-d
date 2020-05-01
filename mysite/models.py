from django.db import models

class ClientInfo(models.Model) :
	client_nom = models.CharField(max_length=200)
	client_tel = models.CharField(max_length=200)
	client_mail = models.CharField(max_length=200)
	client_adresse = models.CharField(max_length=200)

	def __str__(self) :
		return self.client_nom


class FournisseurInfo(models.Model) :
	fournisseur_nom = models.CharField(max_length=200)
	fournisseur_tel = models.CharField(max_length=200)
	fournisseur_mail = models.CharField(max_length=200)
	fournisseur_adresse = models.CharField(max_length=200)

	def __str__(self) :
		return self.fournisseur_nom


class EntreeInfo(models.Model) :
	entree_date = models.CharField(max_length=200)
	entree_fournisseur = models.CharField(max_length=200)
	entree_produit = models.CharField(max_length=200)
	entree_quantite = models.CharField(max_length=200)

	def __str__(self) :
		return self.entree_date


class SortieInfo(models.Model) :
	sortie_date = models.CharField(max_length=200)
	sortie_fournisseur = models.CharField(max_length=200)
	sortie_produit = models.CharField(max_length=200)
	sortie_quantite = models.CharField(max_length=200)

	def __str__(self) :
		return self.sortie_date


class ProduitInfo(models.Model) :
	produit_designation = models.CharField(max_length=200)
	produit_categorie = models.CharField(max_length=200)
	produit_etat_stock = models.CharField(max_length=200)
	produit_prix_achat = models.CharField(max_length=200)
	produit_prix_vente = models.CharField(max_length=200)

	def __str__(self) :
		return self.produit_designation

		
class UtilisateurInfo(models.Model) :
	utilisateur_nom = models.CharField(max_length=200)
	utilisateur_prenom = models.CharField(max_length=200)
	utilisateur_dernier_cnx = models.CharField(max_length=200)
	utilisateur_mdp = models.CharField(max_length=200)

	def __str__(self) :
		return self.utilisateur_nom

