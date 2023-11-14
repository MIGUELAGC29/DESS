from django.shortcuts import render
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from Login.models import Usuario, UnidadAcademica, ProgramaAcademico, NivelAcademico, Cuestionario, Edad, Pais, Ciudad


def peticionCurp(request):
    return render(request, 'pedirCurp.html')


def registroUsuario(request):
    
    url = "https://api.plataforma.ipn.mx/publico/general/secure/renapo/curp/consultar"
    user = "deyssuser"
    password = "p5HHNbdq7JUt5Hnqwv2erWva6hPbKtk8"
    
    if request.method == "POST":
        curp = request.POST['curp']
        json = "{" + "\"data\":{" + "\"curp\":" + "\"" + curp + "\"" + "} }"
        request_renapo = requests.post(url, auth = HTTPBasicAuth(user, password), data=json)
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
                    #Verificar curp existente o no
                    validaCurp = Usuario.objects.filter(curp = curp).exists()
                    if validaCurp:
                        error = "Usuario ya registrado"
                        return render(request, 'pedirCurp.html', {
                            'error':error,
                            'value':curp,
                            })
                    else:
                        nombres = jsonData.get('nombres')
                        ap_paterno = jsonData.get('apellido1')
                        ap_materno = jsonData.get('apellido2')
                        
                        unidades_academicas = UnidadAcademica.objects.all()
                        programas_academicos = ProgramaAcademico.objects.all()
                        niveles_academicos = NivelAcademico.objects.all()
                        edades = Edad.objects.all()
                        paises = Pais.objects.all()
                        ciudades = Ciudad.objects.all()
                        alcaldias_municipios = Ciudad.objects.all()

                        return render(request, 'registroUsuario.html', {
                            'curp': curp,
                            'nombres': nombres,
                            'ap_paterno': ap_paterno,
                            'ap_materno': ap_materno,
                            'unidades_academicas': unidades_academicas,
                            'programas_academicos': programas_academicos,
                            'niveles_academicos': niveles_academicos,
                            'edades': edades,
                            'paises': paises,
                            'ciudades': ciudades,
                            'alcaldias_municipios':alcaldias_municipios,
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
        
        usuario = Usuario(nombre = request.POST['nombres'],
                          apellido1 = request.POST['apellido1'],
                          apellido2 = request.POST['apellido2'],
                          curp = request.POST['curp'],
                          genero = request.POST['genero'],
                          estado_civil = request.POST['estado_civil'],
                          email = request.POST['email'],
                          telefono = request.POST['telefono'],
                          codigo_postal = request.POST.get('codigo_postal', None),
                          ciudad = request.POST['entidad_federativa'],
                          alcaldia_municipio = request.POST.get('alcaldia_municipio', None),
                          boleta = request.POST['boleta'],
                          id_na = NivelAcademico.objects.get(id_na = int(request.POST.get('nivel_academico'))),                          
                          id_ua = UnidadAcademica.objects.get(id_ua = request.POST['unidad_academica']),
                          id_pa = ProgramaAcademico.objects.get(id_pa = request.POST['programa_academico']),
                          id_edad = Edad.objects.get(id_edad = request.POST['edad']),
                          id_pais_nacimiento = Pais.objects.get(id_pais = request.POST['pais_nacimiento']),
                          id_pais_residencia = Pais.objects.get(id_pais = request.POST['pais_residencia']))
        
        usuario.save()
        #print(usuario.id_usuario)
        if int(request.POST.get('nivel_academico')) == 1:
            cuestionarios = Cuestionario.objects.filter(id_na = int(request.POST.get('nivel_academico')))
            return render(request, 'Cuestionario/seleccionCuestionarioMedioSuperior.html', {
                'cuestionarios': cuestionarios,
            })
        elif int(request.POST.get('nivel_academico')) == 2:            
            cuestionarios = Cuestionario.objects.filter(id_na = int(request.POST.get('nivel_academico')))
            return render(request, 'seleccionCuestionarioSuperior.html', {
                'cuestionarios': cuestionarios,
                'id_usuario' : usuario.id_usuario,
            })
            
    return render
