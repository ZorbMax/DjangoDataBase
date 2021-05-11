from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('register/',views.register),
    path('register_epidemiologiste/',views.register_epidemiologiste),
    path('login/',views.login),
    path('utilisateur/',views.user),
    path('epidemiologiste/',views.epidemio)
]