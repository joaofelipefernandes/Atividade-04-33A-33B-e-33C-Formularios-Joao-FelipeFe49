from django.db import models

class Jogadores(models.Model):
  nome= models.CharField(max_length=50)
  exclube= models.CharField(max_length=50)
  idade= models.CharField(max_length=50)
  duracaocontrato= models.CharField(max_length=50)
class Contratacoes(models.Model):
  POSICAO= [
    ("G","Goleiro"),
    ("L","Lateral"),
    ("Z","Zagueiro"),
    ("V","Volante"),
    ("M","Meia"),
    ("A","Atacante"),
  ]
  nome= models.CharField(max_length=50)
  valor= models.CharField(max_length=50)
  posicao= models.CharField(max_length=1, choices=POSICAO)