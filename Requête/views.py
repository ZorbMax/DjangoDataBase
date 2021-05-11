from django.shortcuts import render, redirect
from django.http import HttpResponse
from psycopg2._psycopg import cursor
from django.db import connection
from .forms import *

b = connection.cursor()

def index(request):
    requête=Requête.objects.all()
    return render(request,'index.html',{'requête':requête})

def login(request):
    global uuid
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_pseudo = form.cleaned_data.get('pseudo')
            data_mdp = form.cleaned_data.get('mdp')
            b.execute("SELECT id FROM personnes where pseudo = %s AND mdp = %s",[data_pseudo, data_mdp])
            uuid = b.fetchone()
            if uuid:
                b.execute("SELECT id_personnes FROM epidemiologistes where id_personnes = %s", [uuid])
                if uuid == b.fetchone():
                    return redirect('http://127.0.0.1:8000/epidemiologiste')
                return redirect('http://127.0.0.1:8000/utilisateur')
    context={'form':form}
    return render(request,'login.html',context)

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_nom = form.cleaned_data.get('nom')
            data_prenom = form.cleaned_data.get('prenom')
            data_pseudo = form.cleaned_data.get('pseudo')
            data_mdp = form.cleaned_data.get('mdp')
            data_adresse = form.cleaned_data.get('adresse')
            b.execute("INSERT INTO personnes(nom, prenom, pseudo, mdp, adresse) VALUES (%s,%s,%s,%s,%s)", [data_nom, data_prenom, data_pseudo, data_mdp, data_adresse])
            return redirect('http://127.0.0.1:8000/login')
    context={'form':form}
    return render(request,'register.html',context)

def register_epidemiologiste(request):
    form = RegisterFormEpidemio()
    if request.method == 'POST':
        form = RegisterFormEpidemio(request.POST)
        if form.is_valid():
            data_nom = form.cleaned_data.get('nom')
            data_prenom = form.cleaned_data.get('prenom')
            data_pseudo = form.cleaned_data.get('pseudo')
            data_mdp = form.cleaned_data.get('mdp')
            data_adresse = form.cleaned_data.get('adresse')
            data_centre = form.cleaned_data.get('centre')
            data_tel = form.cleaned_data.get('tel_service')
            b.execute("INSERT INTO personnes(nom, prenom, pseudo, mdp, adresse) VALUES (%s,%s,%s,%s,%s)", [data_nom, data_prenom, data_pseudo, data_mdp, data_adresse])
            b.execute("SELECT id FROM personnes WHERE nom = %s AND prenom = %s AND pseudo = %s",[data_nom, data_prenom, data_pseudo])
            id = b.fetchone()
            b.execute("INSERT INTO epidemiologistes(id_personnes, centre, tel_service) VALUES (%s,%s,%s)", [id, data_centre, data_tel])
            return redirect('http://127.0.0.1:8000/login')
    context={'form':form}
    return render(request,'register_epidemio.html',context)

def user(request):
    context={}
    return render(request,'user.html',context)

def epidemio(request):
    context={}
    return render(request,'epidemio.html',context)