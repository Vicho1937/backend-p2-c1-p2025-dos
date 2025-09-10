from django.http import HttpResponse

def inicio(request):
    nombre = "Vicente Garcia"
    return HttpResponse(f"¡Bienvenidos a mi primera app django, {nombre}!")