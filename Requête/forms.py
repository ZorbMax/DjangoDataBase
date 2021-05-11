from django import forms


class RegisterForm(forms.Form):
    nom = forms.CharField(label='Nom',max_length=20)
    prenom = forms.CharField(label='Prenom',max_length=20)
    pseudo = forms.CharField(label='Pseudo',max_length=20)
    mdp = forms.CharField(label='Mot de passe',max_length=20)
    adresse = forms.CharField(label="Adresse",max_length=100)

class RegisterFormEpidemio(forms.Form):
    nom = forms.CharField(label='Nom',max_length=20)
    prenom = forms.CharField(label='Prenom',max_length=20)
    pseudo = forms.CharField(label='Pseudo',max_length=20)
    mdp = forms.CharField(label='Mot de passe',max_length=20)
    adresse = forms.CharField(label="Adresse",max_length=100)
    centre = forms.CharField(label="Centre",max_length=20)
    tel_service = forms.CharField(label="Numéro de téléphone")

class LoginForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=20)
    mdp = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(),max_length=20)