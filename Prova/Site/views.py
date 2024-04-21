from django.shortcuts import render, redirect
from .models import Nota

def index(request):
    notas = Nota.objects.all()
    return render(request, 'index.html', {'notas': notas})

def salvar_nota(request):
    if request.method == 'POST':
        nota_texto = request.POST.get('nota', '')
        Nota.objects.create(texto=nota_texto)
    return redirect('index')