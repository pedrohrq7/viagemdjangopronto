from django.shortcuts import render
from cadastro.models import Pessoa

# Create your views here.

def cadastro(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Cadastro',
        'pessoas': Pessoa.objects.all(),
    }
    return render(request,
                  'cadastro/index.html',
                  contexto,)

def gravar(request):
    # salvar os dados da tela no banco
    nova_pessoa = Pessoa()
    nova_pessoa.nome     = request.POST.get("nome")
    nova_pessoa.telefone = request.POST.get("movel")
    nova_pessoa.email    = request.POST.get("correio")
    nova_pessoa.save()

    return cadastro(request)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
        request,
        'cadastro/index.html',
        {"pessoa": pessoa},
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.telefone = request.POST.get('movel')
    pessoa.email = request.POST.get('correio')
    pessoa.save()
    return cadastro(request)

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return cadastro(request)

