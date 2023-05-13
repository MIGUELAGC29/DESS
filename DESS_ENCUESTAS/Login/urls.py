from django.urls import path
from Login.views import *


urlpatterns = [
    path('', peticionCurp, name="PeticionCurp"),
    path('registro/', registroUsuario, name="Registro_Usuario"),
    path('guardarUsuario/', guardarUsuario, name="Guardar_Usuario"),
]
