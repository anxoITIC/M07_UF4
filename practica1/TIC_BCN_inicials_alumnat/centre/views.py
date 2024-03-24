from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
from django.shortcuts import render
from .forms import PersonForm



def index(request):
    professor = {"name": "Roger", "surname": "Sobrino", "age": "42"}
    return render(request, 'index_centre.html', {'nombre': professor["name"], 'surname': professor["surname"], 'age': professor["age"]})

def proff(request):
    professors = [
        {"id": "1", "name": "Roger", "surname": "Sobrino", "age": "42", "rol": "m07", "curs": "DAW2"},
        {"id": "2", "name": "Lionel", "surname": "Messi", "age": "36", "rol": "Barça", "curs": "DAW2"},
        {"id": "3", "name": "Juanma", "surname": "No disponible", "age": "53", "rol": "m06", "curs": "DAW2"},
        {"id": "4", "name": "Leonardo", "surname": "Di Caprio", "age": "53", "rol": "m06", "curs": "DAW2"}
    ]
    return render(request, 'proff.html', {'professors': professors})

def users(request):
    alumne = [
        {"id": "1", "name": "Anxo", "surname": "Aragundi", "age": "20", "rol": "atractiu", "curs": "DAW2"},
        {"id": "2", "name": "Carlos Andrés", "surname": "Zambrano", "age": "24", "rol": "cregut", "curs": "DAW2"},
        {"id": "3", "name": "Eric", "surname": "Sánchez", "age": "19", "rol": "no fa gràcia", "curs": "DAW2"},
        {"id": "4", "name": "Joel", "surname": "Ghanem", "age": "19", "rol": "pesat", "curs": "DAW2"},
        {"id": "5", "name": "Jun", "surname": "No el se escriure", "age": "20", "rol": "estudiant", "curs": "DAW2"},
        {"id": "6", "name": "Lamine", "surname": "Yamal", "age": "16", "rol": "baller", "curs": "DAW2"},
        {"id": "7", "name": "Jules", "surname": "Koundé", "age": "24", "rol": "flow", "curs": "DAW2"}
    ]
    return render(request, 'users.html', {'alumne': alumne})

def info_user(request, user_id):
    alumne = [
        {"id": "1", "name": "Anxo", "surname": "Aragundi", "age": "20", "rol": "atractiu", "curs": "DAW2"},
        {"id": "2", "name": "Carlos Andrés", "surname": "Zambrano", "age": "24", "rol": "cregut", "curs": "DAW2"},
        {"id": "3", "name": "Eric", "surname": "Sánchez", "age": "19", "rol": "no fa gràcia", "curs": "DAW2"},
        {"id": "4", "name": "Joel", "surname": "Ghanem", "age": "19", "rol": "pesat", "curs": "DAW2"},
        {"id": "5", "name": "Jun", "surname": "No el se escriure", "age": "20", "rol": "estudiant", "curs": "DAW2"},
        {"id": "6", "name": "Lamine", "surname": "Yamal", "age": "16", "rol": "baller", "curs": "DAW2"},
        {"id": "7", "name": "Jules", "surname": "Koundé", "age": "24", "rol": "flow", "curs": "DAW2"}
    ]

    alumne_seleccionat = None
    for user in alumne:
        if user['id'] == str(user_id):
            alumne_seleccionat = user
            break

    return render(request, 'info_user.html', {'alumne': alumne_seleccionat})

def info_prof(request, professor_id):
    professors = [
        {"id": "1", "name": "Roger", "surname": "Sobrino", "age": "42", "rol": "m07", "curs": "DAW2"},
        {"id": "2", "name": "Lionel", "surname": "Messi", "age": "36", "rol": "Barça", "curs": "DAW2"},
        {"id": "3", "name": "Juanma", "surname": "No disponible", "age": "53", "rol": "m06", "curs": "DAW2"},
        {"id": "4", "name": "Leonardo", "surname": "Di Caprio", "age": "53", "rol": "m06", "curs": "DAW2"}
    ]

    profe_concret = None
    for professor in professors:
        if professor['id'] == str(professor_id):
            profe_concret = professor
            break

    return render(request, 'info_prof.html', {'professor': profe_concret})


#per renderitzar el formulari
def formulari(request):
    formulari = PersonForm()
    context = {'form':formulari}
    return render(request, 'formulari.html', context)