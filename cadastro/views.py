from django.shortcuts import render
from templates import *
# Create your views here.
def cadastro(request):
    return render(request, "cadastro.html")