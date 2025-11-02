from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, "home.html")

def films(request):
    filmebi = ["vikings", "The Last Kingdom", "Mission Imposible"]

    ratings = [10, 10, 10]

    filme = zip(filmebi, ratings)
                
    return render(request, 'films.html', {'filme' : filme})