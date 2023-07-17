from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Movie

def fetch_movie_recommendations(genre):
    url = f"https://www.imdb.com/search/title/?genres={genre}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_tags = soup.select('.lister-item.mode-advanced')
    movies = []
    for tag in movie_tags:
        title = tag.select_one('.lister-item-header a').text.strip()
        rating_tag = tag.select_one('.ratings-imdb-rating strong')
        rating = rating_tag.text.strip() if rating_tag else 'N/A'
        if rating != 'N/A':
            poster = tag.select_one('.lister-item-image img')['loadlate']
            description = tag.select_one('.lister-item-content .text-muted').text.strip()
            movies.append({
                'Title': title,
                'Rating': rating,
                'Poster': poster,
                'Description': description
            })
    sorted_movies = sorted(movies, key=lambda x: float(x['Rating']), reverse=True)
    return sorted_movies

def get_movie_recommendations(request):
    genre = request.GET.get('genre', '')
    movies = fetch_movie_recommendations(genre)
    context = {'movies': movies}
    return render(request,'movie_recommendations.html',context)