from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def depositar(request):
    return render(request, 'depositar.html')

def sacar(request):
    return render(request, 'sacar.html')

def iniciar_jogo(request):
    novo_jogo = {'estado': 'Novo'}
    return JsonResponse(novo_jogo)