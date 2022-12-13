from django.shortcuts import render
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth


def peticionCurp(request):
    return render(request, 'pedirCurp.html')


def registroUsuario(request):
    
    url = "https://api.plataforma.ipn.mx/publico/general/secure/renapo/curp/consultar"
    user = "deyssuser"
    password = "p5HHNbdq7JUt5Hnqwv2erWva6hPbKtk8"
    
    if request.method == "POST" or request.method == "GET":
        curp = request.POST['curp']
        json = "{" + "\"data\":{" + "\"curp\":" + "\"" + curp + "\"" + "} }"
        request_renapo = requests.post(url, auth = HTTPBasicAuth(user,password), data=json)
        if(request_renapo != None):
            try:
                jsonData = request_renapo.json()
                if(jsonData.get('@statusOper') == "NO EXITOSO"):
                    error = jsonData.get('@message')
                    return render(request, 'pedirCurp.html', {
                    'error':error,
                    'value':curp,
                    })
                elif(jsonData.get('@statusOper') == "EXITOSO"):
                    nombres = jsonData.get('nombres')
                    ap_paterno = jsonData.get('apellido1')
                    ap_materno = jsonData.get('apellido2')
                    return render(request, 'registroUsuario.html', {
                        'curp': curp,
                        'nombres': nombres,
                        'ap_paterno': ap_paterno,
                        'ap_materno': ap_materno,    
                        })
            except:
                error = "SOLICITUD NO REALIZADA, INTENTELO MÁS TARDE1"
                return render(request, 'pedirCurp.html', {
                    'error':error,
                    'value':curp,
                    })
        else:
            error = "SOLICITUD NO REALIZADA, INTENTELO MÁS TARDE2"
            return render(request, 'pedirCurp.html', {
                'error':error,
                'value':curp,
                })
            
            
            
#def guardarUsuario(request):