from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    movies = retrieveMoviesFromGhibliAPI()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def retrieveMoviesFromGhibliAPI():
    # to show the API is called only once a minute
    print('Calling Ghibli API')

    films = requests.get('https://ghibliapi.herokuapp.com/films/').json()
    peopleList = requests.get('https://ghibliapi.herokuapp.com/people/').json()

    for film in films:
        film['people'] = []

    for people in peopleList:
        for film_url in people['films']:
            next(filter(lambda film: film['url'] == film_url, films))['people'].append(people)

    return films
