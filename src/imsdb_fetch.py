import random
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://imsdb.com/"
ALL_SCRIPTS = "all-scripts.html"
SCRIPT_BASE = "scripts/"


class ScriptNotFoundException(Exception):
    """Exception thrown when script could not be found"""
    pass


class MoviesNotFoundException(Exception):
    """Exception thrown when movies could not be found"""
    pass


def fetchMovieTitles():
    page = requests.get(BASE_URL + ALL_SCRIPTS)
    soup = BeautifulSoup(page.content, "html.parser")

    tableMovieEntries = soup.find_all('p')

    movieTitles = []
    for p in tableMovieEntries:
        movieTitles.append(p.find('a', href=True).contents[0])

    if len(movieTitles) <= 0:
        raise MoviesNotFoundException

    return movieTitles


def pickRandomMovie():
    movies = fetchMovieTitles()
    return random.choice(movies)


def getMovieScript(movieTitle=pickRandomMovie()):
    parsedMovieTitle = movieTitle.replace(' ', '-')
    page = requests.get(BASE_URL + SCRIPT_BASE + parsedMovieTitle + '.html')

    soup = BeautifulSoup(page.content, "html.parser")
    script = soup.find(class_="scrtext").find('pre').text

    if len(script) <= 0:
        raise ScriptNotFoundException

    return script
