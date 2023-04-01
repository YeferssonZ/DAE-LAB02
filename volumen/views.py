from django.shortcuts import render

def index(request):
    context = {
        'titulo': "volumen",
    }
    return render(request, 'volumen/volumen.html', context)

def volumen(request):
    return render(request, 'volumen.html')
