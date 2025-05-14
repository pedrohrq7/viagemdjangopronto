from django.shortcuts import render

# Create your views here.
def destinos(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Destinos'
    }
    return render(request, 
                  'destinos/index.html',
                  contexto,)