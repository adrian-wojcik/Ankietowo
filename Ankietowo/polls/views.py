from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Witaj , tutaj będzie widok kiedyś jak się za to zabierzemy XD </h1>")