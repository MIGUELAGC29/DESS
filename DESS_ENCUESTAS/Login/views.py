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
        request = requests.post(url, auth = HTTPBasicAuth(user,password), data=json)
        if(request != None):
            try:
                jsonData = request.json()
                nombres = jsonData.get('nombres')
                ap_paterno = jsonData.get('apellido1')
                ap_materno = jsonData.get('apellido2')
                return render(request, 'registroUsuario.html', {
                'curp': curp,
                'nombres': nombres,
                'ap_paterno': ap_paterno,
                'ap_materno': ap_materno,    })
            except:
                print("NO GENIAL")
        else:
            messages.add_message(request=request, level=messages.ERROR, message="SOLICITUD NO REALIZADA, INTENTELO MÁS TARDE")
            return render(request, 'pedirCurp.html', {
                'error':error,
                'value':curp,
            })











import base64
import requests 
from requests.auth import HTTPBasicAuth


url = "https://api.plataforma.ipn.mx/publico/general/secure/renapo/curp/consultar"
user = "deyssuser"
password = "p5HHNbdq7JUt5Hnqwv2erWva6hPbKtk8"
curp = "MACA870610MDFTSD01"



json = "{" + "\"data\":{" + "\"curp\":" + "\"" + curp + "\"" + "} }"
request = requests.post(url, auth = HTTPBasicAuth(user,password), data=json)
if(request != None):
    try:
        jsonData=request.json()
        print(jsonData.get('nombres'))
    except:
        print("NO GENIAL")

    





        
            
            

        


    
  