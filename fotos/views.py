from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def fotos(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Fotos'
    }
    return render(request, 
                  'fotos/index.html',
                  contexto,)