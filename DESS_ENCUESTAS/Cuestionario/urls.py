from django.urls import path
from Cuestionario.views import *


urlpatterns = [
    path('seleccionCuestionario/<str:cuestionario>', seleccionCuestionario, name="Seleccion_Cuestionario"),
]
