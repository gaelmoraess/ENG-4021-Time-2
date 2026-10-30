from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'home.html')

def ComoUsar(request):


    return render(request, 'ComoUsar.html')


def EsqueciSenha (request):


    return render(request, 'EsqueciSenha.html')

def CriacConta (request):


    return render(request, 'CriarConta.html')

def Artigos (request):


    return render(request, 'Artigos.html')

def EdicaoUsuario(request):

    return render(request, 'EdicaoUsuario.html')

def RemocaoUsuario(request):

    return render(request, 'RemocaoUsuario.html')

def Tela(request):


    return render(request, 'Tela.html')

def HistoricoFamiliar(request):

    return render(request, 'HistoricoFamiliar.html')

def ListarUsuarios(request):

    return render(request, 'ListarUsuarios.html')


def CalendarioCuidados(request):

    return render(request, 'CalendarioCuidados.html')

# View de renderização de interface — Sprint 7.
def RelatorioPreventivo(request):
    return render(request, 'RelatorioPreventivo.html')

# Interface de Perfil de Saúde; dados não são persistidos.
def PerfilSaude(request):
    return render(request, 'PerfilSaude.html')

# Página de consentimento de dados (interface demonstrativa).
def ConsentimentoDados(request):
    return render(request, 'ConsentimentoDados.html')

# Preferências de notificações (interface demonstrativa).
def PreferenciasNotificacoes(request):
    return render(request, 'PreferenciasNotificacoes.html')

# View para renderizar a tela do Check-up Inteligente.
def CheckupInteligente(request):
    return render(request, 'CheckupInteligente.html')
