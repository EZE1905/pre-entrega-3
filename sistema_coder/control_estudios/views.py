from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from control_estudios.forms import equipoFormulario

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response


def inicio(request):

    return HttpResponse("vista al inicio")


def listar_jugadores(request):
    contexto = {
        "jugadores": [
            {"nombre": "Lionel", "apellido": "Messi"},
            {"nombre": "Manuela", "apellido": "Gomez"},
            {"nombre": "Ivan", "apellido": "Tomasevich"},
            {"nombre": "Carlos", "apellido": "Perez"},
        ]
    }
    http_response = render(
        request=request,
        template_name='appcoder/listar_jugadores.html',
        context=contexto,
    )
    return http_response


def equipo(request):

    return HttpResponse("vista a los equipos")


def estadio(request):

    return HttpResponse("vista a los estadios")


def crear_equipo(request):
    if request.method == "POST":
        formulario = equipoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            liga = data["liga"]
            equipo = equipo(nombre=nombre, liga=liga)  # lo crean solo en RAM
            equipo.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('equipos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = equipoFormulario()
    http_response = render(
        request=request,
        template_name='appcoder/formulario_equipo.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_equipo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        equipo = equipo.objects.filter(comision__contains=busqueda)
        contexto = {
            "equipo": equipo,
        }
       
        http_response = render(
            request=request,
            template_name='appcoder/equipos.html',
            context=contexto,
                )
        return http_response
