from django.db import models
from django import forms

# Create your models here.
inclusividad=[
    ("si","Si"),
    ("no","No"),
]

tiposalaChoice=[
    ("normal","Normal"),
    ("premiun","Premiun"),
    ("vip","Vip")
]
estadosalaChoice=[
    ("disponible","Disponible"),
    ("ocupado","Ocupado"),
]




class Sala(models.Model):
    CantidadSilla=models.PositiveIntegerField()
    NumeroSala=models.CharField(max_length=7)
    TamanioPantalla=models.CharField(max_length=30)
    InclusividadSala=models.BooleanField(default=True,max_length=10)#ChoiceField(widget=forms.RadioSelect(choices=inclusividadChoice))
    TipoSala=models.CharField(max_length=10,choices=tiposalaChoice)
    EstadoSala=models.CharField(max_length=10,choices=estadosalaChoice)
