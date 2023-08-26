from django.urls import path
from Cuestionario.views import *


urlpatterns = [
    path('seleccionCuestionario/<str:id_cuestionario>/<str:id_usuario>/', seleccionCuestionarioS, name="Seleccion_Cuestionario_S"),
    path('finalizadoCuestionarioTransversal/<str:id_usuario>/', finalizadoCuestionarioTransversal, name = "Finalizado_Cuestionario_Transversal")
]
