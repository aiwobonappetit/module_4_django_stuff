from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='background-color: lightblue; text-align: center;'>Домашка по 4 занятию</h1>")