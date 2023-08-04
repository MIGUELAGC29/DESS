from django.shortcuts import render

# Create your views here.
def seleccionCuestionario(request, cuestionario):
    
    cuestionario_nombre = cuestionario

        
    return render(request, 'Cuestionario_1.html', {'cuestionario_nombre':cuestionario_nombre,})