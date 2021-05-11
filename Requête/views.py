from django.shortcuts import render, redirect
from django.http import HttpResponse
from psycopg2._psycopg import cursor
from django.db import connection
from .models import *
from .forms import *

b = connection.cursor()

def index(request):
    f = open('UUID.txt')
    uuid = f.read()
    f.close()
    if not uuid:
        context={}
        return render(request,'index.html',context)
    else:
        return redirect('http://127.0.0.1:8000/login')

def login(request):
    f = open('UUID.txt')
    uuid = f.read()
    f.close()
    if uuid == "":
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data_pseudo = form.cleaned_data.get('pseudo')
                data_mdp = form.cleaned_data.get('mdp')
                b.execute("SELECT id FROM personnes where pseudo = %s AND mdp = %s", [data_pseudo, data_mdp])
                id = b.fetchone()
                if id is not None:
                    uuid = str(id[0])
                    f = open('UUID.txt', 'w')
                    f.write(uuid)
                    f.close()
                    b.execute("SELECT id_personnes FROM epidemiologistes where id_personnes = %s", [uuid])
                    if b.fetchone() is None:
                        return redirect('http://127.0.0.1:8000/utilisateur')
                    else:
                        return redirect('http://127.0.0.1:8000/epidemiologiste')
        context = {'form': form}
        return render(request, 'login.html', context)
    else:
        b.execute("SELECT id_personnes FROM epidemiologistes where id_personnes = %s", [uuid])
        if b.fetchone() is None:
            return redirect('http://127.0.0.1:8000/utilisateur')
        else:
            return redirect('http://127.0.0.1:8000/epidemiologiste')


def logout(request):
    f = open('UUID.txt', 'w')
    f.write("")
    f.close()
    return redirect('http://127.0.0.1:8000')

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
    f = open('UUID.txt')
    uuid = f.read()
    f.close()
    if uuid:
        b.execute("SELECT id_personnes FROM epidemiologistes where id_personnes = %s", [uuid])
        if not b.fetchone():
            form = SQLForm()
            reponse = ""
            table = ""
            if request.method == 'POST':
                form = SQLForm(request.POST)
                if form.is_valid():
                    SQL = form.cleaned_data.get('SQL')
                    if not any(x in SQL.lower() for x in ['insert', 'alter', 'create', 'drop', 'update', 'delete']):
                        if SQL.split()[0].lower() == 'select':
                            b.execute(SQL)
                            table = b.fetchall()
                        else:
                            reponse = "Ce n'est pas une commande reconnue"
                    else:
                        reponse = 'Vous ne disposez des autorisations nécessaires'
            context = {'form': form, 'table':table, 'reponse': reponse}
            return render(request, 'user.html', context)
        else:
            return redirect('http://127.0.0.1:8000/epidemiologiste')
    else:
        return redirect('http://127.0.0.1:8000')


def epidemio(request):
    f = open('UUID.txt')
    uuid = f.read()
    f.close()
    if uuid:
        b.execute("SELECT id_personnes FROM epidemiologistes where id_personnes = %s", [uuid])
        if b.fetchone():
            form = SQLForm()
            reponse = ""
            table = ""
            if request.method == 'POST':
                form = SQLForm(request.POST)
                if form.is_valid():
                    SQL = form.cleaned_data.get('SQL')
                    if SQL.split()[0].lower() in ['select', 'insert', 'alter', 'create', 'drop', 'update', 'delete']:
                        b.execute(SQL)
                        if 'select' in SQL.lower():
                            table = b.fetchall()
                        else:
                            reponse = 'Commande bien exécutée'
                    else:
                        reponse = "Ce n'est pas une commande reconnue"
            context={'form':form,'reponse':reponse, 'uuid':uuid, 'table':table}
            return render(request,'epidemio.html',context)
        else:
            return redirect('http://127.0.0.1:8000/utilisateur')
    else:
        return redirect('http://127.0.0.1:8000')