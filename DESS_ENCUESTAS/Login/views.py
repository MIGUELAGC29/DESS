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
        nombres = request.POST['nombres']
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        curp = request.POST['curp']
        edad = request.POST['edad']
        genero = request.POST['genero']
        estado_civil = request.POST['estado_civil']
        email = request.POST['email']
        telefono = request.POST['telefono']
        pais_nacimiento = request.POST['pais_nacimiento']
        pais_residencia = request.POST['pais_residencia']
        entidad_federativa = request.POST['entidad_federativa']
        alcaldia_municipio = request.POST.get('alcaldia_municipio', None)
        codigo_postal = request.POST.get('codigo_postal', None)
        nivel_academico = int(request.POST.get('nivel_academico'))
        unidad_academica = request.POST['unidad_academica']
        programa_academico = request.POST['programa_academico']
        
        print(f"""Nombre: {nombres} \n 
                Apellido Paterno: {apellido1} \n
                Apellido Materno: {apellido2} \n
                Curp: {curp} \n
                Edad: {edad} \n
                Genero: {genero} \n
                Estado Civil: {estado_civil} \n
                Email: {email} \n
                Teléfono: {telefono} \n
                País Nacimiento: {pais_nacimiento} \n
                País Residencia: {pais_residencia} \n
                Entidad Federativa: {entidad_federativa} \n
                Alcaldía/Municipio: {alcaldia_municipio} \n
                Código Postal: {codigo_postal} \n
                Nivel Académico: {nivel_academico} \n
                Unidad Académico: {unidad_academica} \n
                Programa Académico: {programa_academico} \n""")
        
        nivel_academicoD = NivelAcademico.objects.get(id_na = nivel_academico)
        unidad_academicaD = UnidadAcademica.objects.get(id_ua = unidad_academica)
        programa_academicoD = ProgramaAcademico.objects.get(id_pa = programa_academico)
        edadD = Edad.objects.get(id_edad = edad)
        pais_nacimientoD = Pais.objects.get(id_pais = pais_nacimiento)
        pais_residenciaD = Pais.objects.get(id_pais = pais_residencia)
        
        usuario = Usuario(nombre = nombres,
                          apellido1 = apellido1,
                          apellido2 = apellido2,
                          curp = curp,
                          genero = genero,
                          estado_civil = estado_civil,
                          email = email,
                          telefono = telefono,
                          codigo_postal = codigo_postal,
                          ciudad = entidad_federativa,
                          alcaldia_municipio = alcaldia_municipio,
                          id_na = nivel_academicoD,                          
                          id_ua = unidad_academicaD,
                          id_pa = programa_academicoD,
                          id_edad = edadD,
                          id_pais_nacimiento = pais_nacimientoD,
                          id_pais_residencia = pais_residenciaD)
        
        usuario.save()
        
        if alcaldia_municipio is None or len(alcaldia_municipio) == 0:
            print("La variable es una cadena vacía o nula.")
        else:
            print("La variable no es una cadena vacía.")
        
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
