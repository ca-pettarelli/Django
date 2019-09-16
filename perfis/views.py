from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Caroline', 'carol@usp.br', '9879878', 'nenhuma')
    
    if perfil_id == '13':
        perfil = Perfil('Gabriel', 'gabriel@usp.br', '9809809', 'djjdij')
    return render(request, 'perfil.html', {"perfil" : perfil})