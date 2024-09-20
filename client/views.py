from django.shortcuts import render,redirect
from django.views import View
from .models import Client,Compte,Machine,Minage,Achat
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone
from datetime import timedelta
from emailapp.utils import send_email_with_html_body




def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Client.objects.filter(email=email).exists() or Client.objects.filter(telephone=email).exists():
            for cpt in Compte.objects.all():
                if check_password(password,cpt.password):
                    request.session['id_compte'] = cpt.id
                    return redirect('client:produits')
                else:
                    messages.error(request,'Identifiant ou mot de passe incorect')
        else:
            messages.error(request,'Identifiant ou mot de passe incorect')
                       
    return render(request,'login.html')

def register(request):
    context={
        'nom':'',
        'email':'',
        'tel':'',
    }
    if(request.method=='POST'):
        nom=request.POST['nom']
        email=request.POST['email']
        tel=request.POST['tel']
        par=request.POST['par']
        password=request.POST['password']
        con_password=request.POST['con_password']
        context={
            'nom':nom,
            'email':email,
            'tel':tel,            
        }
        if (not Client.objects.filter(telephone=par).exists())and len(par)>0:
            messages.error(request,"le parrain mentionné n'existe pas (laisser vide si vous n'en avez pas)")
        elif password!=con_password:
            messages.error(request,'les mots de passes ne sont pas identiques')
        elif len(password) < 8:
            messages.error(request,'le mot de passe est trop court (au moins 8 caractères)')
        elif (str(password).isalpha()) or (str(password).isdecimal()):
            messages.error(request,'le mot de passe doit contenir au moins un chiffre ou une lettre')
        else:
            password=make_password(password)    
            client=Client(nom=nom,email=email,telephone=tel,date_inscription=timezone.now())         
            client.save()
            cpt=Compte(client=client,password=password)
            request.session['id_compte'] = cpt.id
            cpt.save()           
            
            return redirect('client:produits')
    return render(request,'register.html',context)

class validateurNom(View):
    def post(self,request):
        data=json.loads(request.body)
        if not str(data['nom']).replace(" ", "").isalnum():
            return JsonResponse({'error':'Veuillez éviter les caractères spéciaux'})
        if Client.objects.filter(nom=data['nom']).exists():
            return JsonResponse({'error':'Ce nom existe déjà veuillez choisir un autre'})
        return JsonResponse({'valid':True})
class validateurEmail(View):
    def post(self,request):
        data=json.loads(request.body)
        if '@' not in data['email']:
            return JsonResponse({'error':'Veuillez entrer une email valide'})
        if Client.objects.filter(email=data['email']).exists():
            return JsonResponse({'error':'Cette adresse existe déjà'})
        return JsonResponse({'valid':True})
class validateurTelephone(View):
    def post(self,request):
        data=json.loads(request.body)
        if not str(data['telephone']).replace(" ", "").isdecimal():
            return JsonResponse({'error':"Veuillez mettre uniquement les numeros"})
        
        if Client.objects.filter(telephone=data['telephone']).exists():
            return JsonResponse({'error':'Cette adresse existe déjà'})
        return JsonResponse({'valid':True})
def produits(request):
    cpt_id=request.session.get('id_compte')
    if not cpt_id:
        return redirect('client:login')
    else:
        client=Compte.objects.get(id=cpt_id).client
        machines=Machine.objects.all()
    
        return render(request,'produits.html',{'machines':machines,'client':client})

def compte(request,id_clt):
    cpt_id=request.session.get('id_compte')
    if not cpt_id:
        return redirect('client:login')
    else:
        client=Client.objects.get(id=id_clt)
        achats=Achat.objects.filter(client=client)       
        return render(request,'compte.html',{'client':client,'achats':achats})
def logout(request):
    del request.session['id_compte']
    return redirect('client:login')
def achat(request,id_clt,id_mach):
    mach=Machine.objects.get(id=id_mach)
    client=Client.objects.get(id=id_clt)
    compte=Compte.objects.get(client=client)
    
    if compte.solde_deposer >= (mach.periode_minage * mach.montant_a_miner):
        compte.solde_deposer-=mach.montant
        compte.save()
        Achat.objects.create(client=client,machine=mach,date_heure=timezone.now(),solde_miner=0)
        achats=Achat.objects.filter(client=client)
       
        context={'success':"Achat effectué avec success",'client':client,'achats':achats}
    else:
        achats=Achat.objects.filter(client=client)
       
        context={'error':"Impossible d'acheter cette marchine car vous n'avez pas suffisamment d'argent. Veuillez recharger votre compte et réeffectuez l'achat",'client':client,'achats':achats}    
    return render(request,'compte.html',context)

def minage(request,id_ach):

    achat=Achat.objects.get(id=id_ach)
    prochain=timezone.now() + timedelta(days=1)
    Minage.objects.create(achat=achat,montant=achat.machine.montant_a_miner,date_heure=timezone.now())
    achat.prochain_minage=prochain
    achat.solde_miner+=achat.machine.montant_a_miner
    
    achat.client.compte.solde_a_retirer+=achat.machine.montant_a_miner
    achat.client.compte.save()
    achat.save()
    if achat.solde_miner>=(achat.machine.periode_minage * achat.machine.montant_a_miner):
        achat.encours=False
        achat.save()
    return redirect('/compte/'+str(achat.client.pk))
def prochainMin(request,id_ach):
    prochain=Achat.objects.get(id=id_ach).prochain_minage
    return JsonResponse({'date':prochain})
def depot(request):
    cpt_id=request.session.get('id_compte')
    if not cpt_id:
        return redirect('client:login')
    else:
        client=Compte.objects.get(id=cpt_id).client
    return render(request,'depot.html',{'client':client})

def retrait(request):
    cpt_id=request.session.get('id_compte')
    if not cpt_id:
        return redirect('client:login')
    else:
        client=Compte.objects.get(id=cpt_id).client
        if request.method=='POST':
            montant=int(request.POST['montant'])
            numero=request.POST['numero']
            if montant > client.compte.solde_a_retirer:
                messages.error(request,'le montant que vous avez entré est supérieur à ce que vous pouvez retirer')
            else:
                 client.compte.solde_a_retirer-=montant
                 
                 subjet = "Demande de retrait"
                 template = 'email.html'
                 nom=client.nom
    
                 receivers = ['rodeodjoumsi2@gmail.com']
        
                 context={'nom':nom,'montant':montant,'numero':numero}
                 send_email_with_html_body(subjet=subjet,receivers=receivers, template=template,context=context)
                 client.compte.save()
       
                 messages.success(request,'votre demande de retrait a été acceptée. Vous recevrez un depot dans quelques heures')
        
    return render(request,'retrait.html',{'client':client})
    