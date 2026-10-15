from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return self.nome