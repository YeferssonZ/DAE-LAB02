from django.shortcuts import render

def index(request):
    context = {
        'titulo': "calculadora",
    }
    return render(request, 'calculadora/calculadora.html', context)

def enviar(request):
    context = {
        'resultado': request.POST['resultado' ],
    }
    return render(request, 'calculadora/resultado.html', context)
