from django.http import HttpResponse, request
from django.shortcuts import render


def main_side(request):
    return render(request, "base.html")