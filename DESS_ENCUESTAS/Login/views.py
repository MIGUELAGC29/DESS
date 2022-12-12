from django.shortcuts import render


def peticionCurp(request):
    return render(request, 'pedirCurp.html')


def registroUsuario(request):
    if request.method == "POST" or request.method == "GET":
        curp = request.POST['curp']
        #SE HACE EL DESMADRE DE LA RENAPO
        nombre = "Miguel"
        ap_paterno = "González"
        ap_materno = "Cruz"
        
    return render(request, 'registroUsuario.html', {
        'curp': curp,
        'nombre': nombre,
        'ap_paterno': ap_paterno,
        'ap_materno': ap_materno,    })
    
    
def error(request):
    return render(request, 'error.html')