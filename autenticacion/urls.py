from django.urls import path

from .views import registro, cerrar_sesion, logear



urlpatterns = [
   
  
    path('',registro, name="Autenticacion"),

    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

    path('logear',logear, name="logear"),

    
]



