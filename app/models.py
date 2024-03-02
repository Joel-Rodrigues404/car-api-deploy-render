from django.db import models

# Create your models here.


class Car(models.Model):

    CONDICAO = [
        ("O", "OTIMO"),
        ("B", "BOM"),
        ("R", "RUIM"),
        ("P", "PESSIMO"),
    ]
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    condicao = models.CharField(max_length=1, choices=CONDICAO, default="O")
