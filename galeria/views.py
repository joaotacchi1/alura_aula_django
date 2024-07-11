from django.shortcuts import render

def index(request):
    
    dados = {
        1: {
            'nome': 'Nebulosa de Carina',
            'legenda': 'webbtelescope.org / NASA / James Webb'
        },
        2: {
            'nome': 'Galáxia do Sombrero',
            'legenda': 'NASA / Hubble Space Telescope'
        }
    }
    
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')

