from django.shortcuts import render
from Login.models import CuestionarioTransversal, Usuario

#Seleccion de cuestionario por nivel
def seleccionCuestionarioS(request, id_cuestionario, id_usuario):
    
    if(int(id_cuestionario) == 1):
        return render(request, 'Cuestionario_Transversal.html', {
            'id_usuario' : id_usuario,
        })
    #agregar los demas cuestionarios
    
    return render(request, 'Error.html')


#Tabla por cuestionario
def finalizadoCuestionarioTransversal(request, id_usuario):
    if request.method == "POST" or request.method == "GET":
        
        cuestionario = CuestionarioTransversal(id_usuario = Usuario.objects.get(id_usuario = int(id_usuario)),
                                               pregunta_1 = request.POST['pregunta_1'],
                                               pregunta_2 = (request.POST['pregunta_2'] + ": " + request.POST['pregunta_2_otro']) if request.POST.get('pregunta_2', None) == "Otro" else request.POST.get('pregunta_2', None),
                                               pregunta_3 = request.POST['pregunta_3'],
                                               pregunta_4 = request.POST['pregunta_4'],
                                               pregunta_5 = request.POST.get('pregunta_5', None),
                                               pregunta_6 = request.POST['pregunta_6'],
                                               pregunta_7 = request.POST['pregunta_7'],
                                               pregunta_8 = request.POST['pregunta_8'],
                                               pregunta_9 = request.POST['pregunta_9'],
                                               pregunta_10 = (request.POST['pregunta_10'] + ": " + request.POST['pregunta_10_otro']) if request.POST.get('pregunta_10', None) == "Otro" else request.POST.get('pregunta_10', None),
                                               pregunta_11 = (request.POST['pregunta_11'] + ": " + request.POST['pregunta_11_otro']) if request.POST.get('pregunta_11', None) == "Otro" else request.POST.get('pregunta_11', None),
                                               pregunta_12 = (request.POST['pregunta_12'] + ": " + request.POST['pregunta_12_otro']) if request.POST.get('pregunta_12', None) == "Otro" else request.POST.get('pregunta_12', None),
                                               pregunta_13 = request.POST['pregunta_13'],
                                               pregunta_14 = request.POST['pregunta_14'],
                                               pregunta_15 = request.POST['pregunta_15'],
                                               pregunta_16 = request.POST['pregunta_16'],
                                               pregunta_17 = (request.POST['pregunta_17'] + ": " + request.POST['pregunta_17_otro']) if request.POST.get('pregunta_17', None) == "Otro" else request.POST.get('pregunta_17', None),
                                               pregunta_18 = (request.POST['pregunta_18'] + ": " + request.POST['pregunta_18_otro']) if request.POST.get('pregunta_18', None) == "Otro" else request.POST.get('pregunta_18', None),
                                               pregunta_19 = request.POST['pregunta_19'],
                                               pregunta_20 = request.POST['pregunta_20'],
                                               pregunta_21 = request.POST['pregunta_21'],
                                               pregunta_22 = request.POST.get('pregunta_22', None),
                                               pregunta_23 = (request.POST['pregunta_23'] + ": " + request.POST['pregunta_23_otro']) if request.POST.get('pregunta_23', None) == "Otro" else request.POST.get('pregunta_23', None),
                                               pregunta_24 = request.POST.get('pregunta_24', None),
                                               pregunta_25 = request.POST['pregunta_25'],
                                               pregunta_26 = request.POST['pregunta_26'],
                                               pregunta_27 = request.POST['pregunta_27'],
                                               pregunta_28 = request.POST['pregunta_28'],
                                               pregunta_29 = request.POST['pregunta_29'],
                                               pregunta_30 = request.POST['pregunta_30'],
                                               pregunta_31 = request.POST['pregunta_31'],
                                               pregunta_32 = request.POST['pregunta_32'],
                                               pregunta_33 = request.POST['pregunta_33'],
                                               pregunta_34 = request.POST['pregunta_34'],
                                               pregunta_35 = request.POST['pregunta_35'],
                                               pregunta_36 = request.POST['pregunta_36'],
                                               pregunta_37 = request.POST['pregunta_37'],
                                               pregunta_38 = request.POST['pregunta_38'])
        
        cuestionario.save()
        
    return render(request, 'Finaliza.html')