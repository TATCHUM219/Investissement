from django.db import models
from datetime import date
from django.utils import timezone

class Client(models.Model):
    nom=models.CharField(max_length=200,null=False,default='nom')
    date_inscription=models.DateField(null=False,default=timezone.now())   
    telephone=models.CharField(max_length=30,null=False,default='333')
    email=models.EmailField(max_length=100,default='tatchumkamgajordandouglas@gmail.com')
    connecter=models.BooleanField(default=False)
    parain = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return self.nom
    
class Compte(models.Model):
    solde_deposer=models.IntegerField(default=0)
    solde_a_retirer=models.IntegerField(default=0)
    password = models.CharField( max_length=500, null=False)
    client = models.OneToOneField(Client ,on_delete=models.CASCADE, null=False)

class Categorie(models.Model):
    nom=nom=models.CharField(max_length=50)
    def __str__(self):
        return self.nom
class Machine(models.Model):
    nom=models.CharField(max_length=100)
    montant=models.IntegerField()
    periode_minage=models.IntegerField()
    montant_a_miner=models.IntegerField()
    categorie=models.ForeignKey(Categorie,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to='public',null=True,blank=True)
    def __str__(self):
        return self.nom
class Achat(models.Model):
    date_heure=models.DateTimeField()
    solde_miner=models.IntegerField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    machine=models.ForeignKey(Machine,on_delete=models.DO_NOTHING)
    delai=models.DateField(null=False,default=timezone.now())
    prochain_minage=models.DateTimeField(null=False,default=timezone.now())
    encours=models.BooleanField(default=True)
    
class Minage(models.Model): 
    date_heure=models.DateTimeField()
    montant=models.IntegerField()
    achat=models.ForeignKey(Achat,on_delete=models.DO_NOTHING)
class Depot(models.Model):
    date_heure=models.DateTimeField()
    montant=models.IntegerField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
class Retrait(models.Model):
    date_heure=models.DateTimeField()
    montant=models.IntegerField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)


