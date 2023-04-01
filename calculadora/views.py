from django.shortcuts import render

def calculadora(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'calculadora/calculadora.html', context)


def enviar(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operacion = request.POST['operacion']
    resultado = 0
    signo = ""

    if operacion == 'suma':
        resultado = num1 + num2
        signo = "+"
    elif operacion == 'resta':
        resultado = num1 - num2
        signo = "-"
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        signo = "*"
    elif operacion == 'Obligatorio':
        resultado = "?"
        signo = "?"
    else:
        resultado = "nulo"
    context = {
        'titulo': 'Calculadora',
        'num1': request.POST['num1'],
        'num2': request.POST['num2'],
        'operacion': operacion,
        'respuesta': resultado,
        'signo': signo
    }
    return render(request, 'calculadora/resultado.html', context)


