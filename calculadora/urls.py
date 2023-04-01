from django.urls import path
from.import views
app_name = 'calculadora'

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('enviar', views.enviar,  name='enviar'),
]