from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    list_display= ('id','client','solde_deposer','solde_a_retirer','password')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= ('id','nom','date_inscription','connecter','parain', 'telephone', 'email')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display= ('nom',)

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display= ('id','nom','montant','periode_minage','montant_a_miner','categorie')
@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display= ('id','client','machine','solde_miner','date_heure','prochain_minage','encours')
@admin.register(Minage)
class MinageAdmin(admin.ModelAdmin):
    list_display= ('date_heure','achat','montant')
@admin.register(Depot)
class DepotAdmin(admin.ModelAdmin):
    list_display= ('client','date_heure','montant')
@admin.register(Retrait)
class RetraitAdmin(admin.ModelAdmin):
    list_display= ('client','date_heure','montant')