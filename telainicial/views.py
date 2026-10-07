from django.shortcuts import render, redirect
from templates import *
# Create your views here.

def inventario(request):
    if not request.session.get("logado"):
        return redirect("cadastro")
    return render(request, 'inventario.html')