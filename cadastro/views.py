from django.shortcuts import render, redirect
from templates import *
# Create your views here.

senha_padrao = "123"

def cadastro(request):
    if request.method == 'POST':
        senha_digitada = request.POST.get("senha")

        if senha_digitada == senha_padrao:
            request.session["logado"] = True
            return redirect("inventario")
        else:
            context = {"erro": "Senha incorreta"}
            return render(request, "cadastro.html", context)

    return render(request, "cadastro.html")