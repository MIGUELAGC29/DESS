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
        print(id_usuario)
        
        pregunta_1 = request.POST['pregunta_1']
        
        if(request.POST.get('pregunta_2', None) == "Otro"):
            pregunta_2 = request.POST['pregunta_2'] + ": " + request.POST['pregunta_2_otro']
        else:
            pregunta_2 = request.POST.get('pregunta_2', None)
            
        pregunta_3 = request.POST['pregunta_3']
        
        pregunta_4 = request.POST['pregunta_4']
        
        pregunta_5 = request.POST.get('pregunta_5', None)
        
        pregunta_6 = request.POST['pregunta_6']
        
        pregunta_7 = request.POST['pregunta_7']

        pregunta_8 = request.POST['pregunta_8']
        
        pregunta_9 = request.POST['pregunta_9']
        
        if(request.POST['pregunta_10'] == "Otro"):
            pregunta_10 = request.POST['pregunta_10'] + ": " + request.POST['pregunta_10_otro']
        else:
            pregunta_10 = request.POST['pregunta_10']
            
        if(request.POST['pregunta_11'] == "Otro"):
            pregunta_11 = request.POST['pregunta_11'] + ": " + request.POST['pregunta_11_otro']
        else:
            pregunta_11 = request.POST['pregunta_11']
            
        if(request.POST['pregunta_12'] == "Otro"):
            pregunta_12 = request.POST['pregunta_12'] + ": " + request.POST['pregunta_12_otro']
        else:
            pregunta_12 = request.POST['pregunta_12']
            
        pregunta_13 = request.POST['pregunta_13']
        
        pregunta_14 = request.POST['pregunta_14']
        
        pregunta_15 = request.POST['pregunta_15']
        
        pregunta_16 = request.POST['pregunta_16']
        
        if(request.POST['pregunta_17'] == "Otro"):
            pregunta_17 = request.POST['pregunta_17'] + ": " + request.POST['pregunta_17_otro']
        else:
            pregunta_17 = request.POST['pregunta_17']

        if(request.POST['pregunta_18'] == "Otro"):
            pregunta_18 = request.POST['pregunta_18'] + ": " + request.POST['pregunta_18_otro']
        else:
            pregunta_18 = request.POST['pregunta_18']

        pregunta_19 = request.POST['pregunta_19']

        pregunta_20 = request.POST['pregunta_20']
        
        pregunta_21 = request.POST['pregunta_21']
        
        pregunta_22 = request.POST.get('pregunta_22', None)
            
        if(request.POST.get('pregunta_23', None) == "Otro"):
            pregunta_23 = request.POST['pregunta_23'] + ": " + request.POST['pregunta_23_otro']
        else:
            pregunta_23 = request.POST.get('pregunta_23', None)

        pregunta_24 = request.POST.get('pregunta_24', None)
        
        pregunta_25 = request.POST['pregunta_25']
        
        pregunta_26 = request.POST['pregunta_26']

        pregunta_27 = request.POST['pregunta_27']

        pregunta_28 = request.POST['pregunta_28']

        pregunta_29 = request.POST['pregunta_29']

        pregunta_30 = request.POST['pregunta_30']

        pregunta_31 = request.POST['pregunta_31']

        pregunta_32 = request.POST['pregunta_32']

        pregunta_33 = request.POST['pregunta_33']

        pregunta_34 = request.POST['pregunta_34']

        pregunta_35 = request.POST['pregunta_35']

        pregunta_36 = request.POST['pregunta_36']
        
        pregunta_37 = request.POST['pregunta_37']
        
        pregunta_38 = request.POST['pregunta_38']
        
        
        
        print(pregunta_1)
        print(pregunta_2)
        print(pregunta_3)
        print(pregunta_4)
        print(pregunta_5)
        print(pregunta_6)
        print(pregunta_7)
        print(pregunta_8)
        print(pregunta_9)
        print(pregunta_10)
        print(pregunta_11)
        print(pregunta_12)
        print(pregunta_13)
        print(pregunta_14)
        print(pregunta_15)
        print(pregunta_16)
        print(pregunta_17)
        print(pregunta_18)
        print(pregunta_19)
        print(pregunta_20)
        print(pregunta_21)
        print(pregunta_22)
        print(pregunta_23)
        print(pregunta_24)
        print(pregunta_25)
        print(pregunta_26)
        print(pregunta_27)
        print(pregunta_28)
        print(pregunta_29)
        print(pregunta_30)
        print(pregunta_31)
        print(pregunta_32)
        print(pregunta_33)
        print(pregunta_34)
        print(pregunta_35)
        print(pregunta_36)
        print(pregunta_37)
        print(pregunta_38)
        
        cuestionario = CuestionarioTransversal(id_usuario = Usuario.objects.get(id_usuario = int(id_usuario)),
                                               pregunta_1 = pregunta_1,
                                               pregunta_2 = pregunta_2,
                                               pregunta_3 = pregunta_3,
                                               pregunta_4 = pregunta_4,
                                               pregunta_5 = pregunta_5,
                                               pregunta_6 = pregunta_6,
                                               pregunta_7 = pregunta_7,
                                               pregunta_8 = pregunta_8,
                                               pregunta_9 = pregunta_9,
                                               pregunta_10 = pregunta_10,
                                               pregunta_11 = pregunta_11,
                                               pregunta_12 = pregunta_12,
                                               pregunta_13 = pregunta_13,
                                               pregunta_14 = pregunta_14,
                                               pregunta_15 = pregunta_15,
                                               pregunta_16 = pregunta_16,
                                               pregunta_17 = pregunta_17,
                                               pregunta_18 = pregunta_18,
                                               pregunta_19 = pregunta_19,
                                               pregunta_20 = pregunta_20,
                                               pregunta_21 = pregunta_21,
                                               pregunta_22 = pregunta_22,
                                               pregunta_23 = pregunta_23,
                                               pregunta_24 = pregunta_24,
                                               pregunta_25 = pregunta_25,
                                               pregunta_26 = pregunta_26,
                                               pregunta_27 = pregunta_27,
                                               pregunta_28 = pregunta_28,
                                               pregunta_29 = pregunta_29,
                                               pregunta_30 = pregunta_30,
                                               pregunta_31 = pregunta_31,
                                               pregunta_32 = pregunta_32,
                                               pregunta_33 = pregunta_33,
                                               pregunta_34 = pregunta_34,
                                               pregunta_35 = pregunta_35,
                                               pregunta_36 = pregunta_36,
                                               pregunta_37 = pregunta_37,
                                               pregunta_38 = pregunta_38)
        
        cuestionario.save()
        
    return render(request, 'Finaliza.html')