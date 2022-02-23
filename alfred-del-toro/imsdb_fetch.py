import random
import requests
from bs4 import BeautifulSoup

baseURL = "https://imsdb.com/"
allScripts = "all-scripts.html"
scriptBase = "scripts/"

    
def fetchMovieTitles():
    page = requests.get(baseURL + allScripts)
    soup = BeautifulSoup(page.content, "html.parser")

    tableMovieEntries = soup.find_all('p')

    movieTitles = []
    for p in tableMovieEntries:
        movieTitles.append(p.find('a', href=True).contents[0])
    
    return movieTitles

def pickRandomMovie():
    movies = fetchMovieTitles()
    return random.choice(movies)

def getMovieScript(movieTitle = pickRandomMovie()):
    parsedMovieTitle = movieTitle.replace(' ','-')
    page = requests.get(baseURL+scriptBase+parsedMovieTitle+'.html')
    
    soup = BeautifulSoup(page.content, "html.parser")
    script = soup.find(class_="scrtext").find('pre').text

    return script
    