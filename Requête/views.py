from django.shortcuts import render
from .models import Requête

def index(request):
    requête=Requête.objects.all()
    return render(request,'index.html',{'requête':requête})