from django.shortcuts import render
from templates import *
# Create your views here.

def inventario(request):
    return render(request, 'inventario.html')