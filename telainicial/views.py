from templates import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Categoria, Status


def inventario(request):
    if not request.session.get("logado"):
        return redirect("cadastro")

    if request.method == "POST":
        acao = request.POST.get("acao")
        nome = request.POST.get("nome", "").strip()
        id_categoria = request.POST.get("id_categoria")
        id_status = request.POST.get("id_status")
        quantidade = request.POST.get("quantidade")

        if not nome or not id_categoria or not id_status or quantidade in (None, ""):
            messages.error(request, "Preencha todos os campos.")
            return redirect("inventario")

        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                raise ValueError
        except ValueError:
            messages.error(request, "Quantidade inválida.")
            return redirect("inventario")

        categoria = get_object_or_404(Categoria, id=id_categoria)
        status = get_object_or_404(Status, id=id_status)

        if acao == "criar":
            Item.objects.create(
                nome=nome,
                categoria=categoria,
                status=status,
                quantidade=quantidade,
            )
            messages.success(request, f'Item "{nome}" adicionado ao inventário.')

        elif acao == "editar":
            item = get_object_or_404(Item, id=request.POST.get("id"))
            item.nome = nome
            item.categoria = categoria
            item.status = status
            item.quantidade = quantidade
            item.save()
            messages.success(request, f'Item #{item.id} atualizado.')

        else:
            messages.error(request, "Ação inválida.")

        return redirect("inventario")

    itens = Item.objects.select_related("tipo", "categoria", "status").order_by("id")
    categorias = Categoria.objects.order_by("nome")

    return render(request, "inventario.html", {
        "itens": itens,
        "categorias": categorias,
    })