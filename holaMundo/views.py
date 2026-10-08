from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola mundo")
