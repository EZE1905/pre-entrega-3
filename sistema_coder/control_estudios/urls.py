from django.urls import path
from control_estudios.views import (inicio,crear_equipo,listar_jugadores,equipo,estadio,saludar_con_html,buscar_equipo)

urlpatterns = [
    path("listar_jugadores/", view=listar_jugadores),
    path("inicio/", view=inicio),
    path("equipos/", view=equipo),
    path("estadios/", view=estadio),
    path("saludo_html/", saludar_con_html),
    path("crear_equipo/", crear_equipo, name="crear_equipo"),
    path("buscar_equipo/", buscar_equipo, name="buscar_equipo"),
]