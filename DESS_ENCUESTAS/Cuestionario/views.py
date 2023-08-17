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
        
        pregunta_17 = request.POST['pregunta_17']

        pregunta_18 = request.POST['pregunta_18']

        pregunta_19 = request.POST['pregunta_19']

        pregunta_20 = request.POST['pregunta_20']
        
        pregunta_21 = request.POST['pregunta_21']
        
        pregunta_22 = request.POST['pregunta_22']
            

        
        
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
        

        


        
    
    
    
    
    return render(request, 'Finaliza.html')