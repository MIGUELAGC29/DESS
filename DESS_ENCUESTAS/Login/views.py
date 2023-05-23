from django.shortcuts import render
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from Login.models import Usuario, UnidadAcademica, ProgramaAcademico, NivelAcademico, Cuestionario


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
                    
                    unidades_academicas = UnidadAcademica.objects.all()
                    programas_academicos = ProgramaAcademico.objects.all()
                    niveles_academicos = NivelAcademico.objects.all()

                    return render(request, 'registroUsuario.html', {
                        'curp': curp,
                        'nombres': nombres,
                        'ap_paterno': ap_paterno,
                        'ap_materno': ap_materno,
                        'unidades_academicas': unidades_academicas,
                        'programas_academicos': programas_academicos,
                        'niveles_academicos': niveles_academicos,
                        })
            except:
                error = "SOLICITUD NO REALIZADA, INTENTELO MÁS TARDE"
                return render(request, 'pedirCurp.html', {
                    'error':error,
                    'value':curp,
                    })
        else:
            error = "SOLICITUD NO REALIZADA, INTENTELO MÁS TARDE"
            return render(request, 'pedirCurp.html', {
                'error':error,
                'value':curp,
                })
            
            
            
def guardarUsuario(request):
    if request.method == "POST" or request.method == "GET":
        nombres = request.POST['nombres']
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        curp = request.POST['curp']
        sexo = request.POST['sexo']
        edad = request.POST['edad']
        estado_civil = request.POST['estado_civil']
        email = request.POST['email']
        telefono = request.POST['telefono']
        pais = request.POST['pais']
        codigo_postal = request.POST['codigo_postal']
        entidad_federativa = request.POST['entidad_federativa']
        nivel_academico = int(request.POST.get('nivel_academico'))
        alcaldia_municipio = request.POST['alcaldia_municipio']
        unidad_academica = request.POST['unidad_academica']
        programa_academico = request.POST['programa_academico']
        
        print(nombres, apellido1, apellido2, curp, sexo, edad, estado_civil, email, telefono, pais, codigo_postal, entidad_federativa, alcaldia_municipio, nivel_academico, unidad_academica, programa_academico)
        
        if nivel_academico == 1:
            cuestionarios = Cuestionario.objects.filter(id_na = nivel_academico)
            return render(request, 'seleccionCuestionarioMedioSuperior.html', {
                'cuestionarios': cuestionarios,
            })
        elif nivel_academico == 2:
            cuestionarios = Cuestionario.objects.filter(id_na = nivel_academico)
            return render(request, 'seleccionCuestionarioSuperior.html', {
                'cuestionarios': cuestionarios,
            })
            
    return render
