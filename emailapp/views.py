from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse

from datetime import datetime
from client.models import Commande,Ligne_commande
from .utils import send_email_with_html_body
import json
# Create your views here.



class create_view(View):
    """ This view help to create and account for testing sending mails."""
    
   
        
def Email(request):
    return render(request,'email.html')
        