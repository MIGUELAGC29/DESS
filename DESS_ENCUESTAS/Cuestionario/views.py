from django.shortcuts import render

# Create your views here.
def seleccionCuestionario(request, cuestionario):
            
    return render(request, 'Cuestionario_1.html')



def finalizado(request):
    if request.method == "POST" or request.method == "GET":
        pregunta_1 = request.POST['pregunta_1']
        if(request.POST['pregunta_2'] == "Otro"):
            pregunta_2 = request.POST['pregunta_2'] + ": " + request.POST['pregunta_2_otro']
        else:
            pregunta_2 = request.POST['pregunta_2']
        pregunta_3 = request.POST['pregunta_3']
        pregunta_4 = request.POST['pregunta_4']
        pregunta_5 = request.POST['pregunta_5']
        pregunta_6 = request.POST['pregunta_6']
        pregunta_7 = request.POST['pregunta_7']
        pregunta_8 = request.POST['pregunta_8']
        pregunta_9 = request.POST['pregunta_9']
        if(request.POST['pregunta_10'] == "Otro"):
            pregunta_10 = request.POST['pregunta_10'] + ": " + request.POST['pregunta_10_otro']
        else:
            pregunta_10 = request.POST['pregunta_10']

        
        
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

        
    
    
    
    
    return render(request, 'Finaliza.html')