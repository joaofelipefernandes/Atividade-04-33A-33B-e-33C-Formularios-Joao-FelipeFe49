from django.shortcuts import render,redirect
from .models import Jogadores,Contratacoes
# Create your views here.
def home(request):
  Jogadores= Jogadores.objects.all()
  Contratacoes= Contratacoes.objects.all()
  return render(request, "home.html", context={ "Jogadores":Jogadores})
  return render(request, "home.html", context={ "Contratacoes":Contratacoes})

def create_player(request):
  if request.method=="POST"
   Jogadores.objects.create(
     player= request.POST("player")
     number= request.POST("player")
    )
    return redirect("home")
  return render(request, "forms.html", context= {"type": "Adicionar"})

def update_player(request,id):
  player= player.object.get(id = id)
  if request.method=="POST":
     player.name= request.POST["name"]
     player.number= request.POST["number"]
     player.save()
    
    
    return redirect("home")
  return render(request, "forms.html", context= {"type": "Atualizar" "player": player})

def delete_player(request,id):
  player= player.object.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
     player.delete()
    
    
    return redirect("home")
  return render(request, "are you sure.html", context= { "player": player})