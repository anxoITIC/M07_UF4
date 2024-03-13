from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
from django.shortcuts import render

# Create your views here.
def index(request):
    professor = {"name":"Roger", "surname":"Sobrino", "age":"42"}
    return render(request, 'index_centre.html', {'nombre': professor["name"], 'surname': professor["surname"], 'age': professor["age"]})

def proff(request):
    professors = [
        {"id":"1", "name":"Roger", "surname":"Sobrino", "age":"42", "rol":"m07", "curs":"primer"},
        {"id":"2", "name":"Lionel", "surname":"Messi", "age":"36", "rol":"Barça", "curs":"primer"},
        {"id":"3", "name":"Juanma", "surname":"No disponible", "age":"53", "rol":"m06", "curs":"primer"}
    ]
    return render(request, 'proff.html', {'professors': professors})

def users(request):
    students = [
        {"id":"1", "name":"Anxo", "surname":"Aragundi", "age":"20", "rol":"atractiu", "curs":"primer"},
        {"id":"2", "name":"Carlos Andrés", "surname":"Zambrano", "age":"24", "rol":"cregut", "curs":"primer"},
        {"id":"3", "name":"Eric", "surname":"Sánchez", "age":"19", "rol":"no fa gràcia", "curs":"primer"},
        {"id":"4", "name":"Joel", "surname":"Ghanem", "age":"19", "rol":"pesat", "curs":"primer"}
    ]
    return render(request, 'users.html', {'students': students})