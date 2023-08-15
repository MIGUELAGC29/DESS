from django.shortcuts import render

# Create your views here.
def seleccionCuestionario(request, cuestionario):
            
    return render(request, 'Cuestionario_1.html')