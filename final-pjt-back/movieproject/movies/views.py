from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import requests
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer,GenreSerializer
from .models import Movie,Genre,Actor


@api_view(['GET'])
@permission_classes([AllowAny])
def takeMovie(request):
    for i in range(1,21) :
        
        movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR&page={str(i)}'
        movieList = requests.get(movieURL).json()
        results = movieList.get('results')
        genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR'
        genreList = requests.get(genreURL).json()
        genreDatas = genreList.get('genres')
        for genreData in genreDatas:
            Genre.objects.get_or_create(
            id = genreData.get('id'),
            name = genreData.get('name'))

    
        for item in results :
            movieid = item.get('id')
            actorUrl = f'https://api.themoviedb.org/3/movie/{movieid}/credits?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&region=KR&language=ko'
            title = item.get('title')
            release_date = item.get('release_date')
            poster_path = item.get('poster_path')
            overview = item.get('overview')
            vote_avereage = item.get('vote_average')
            original_title = item.get('original_title')
            genreItems = item.get('genre_ids')
            movie = Movie()
            movie.title = title
            movie.release_date = release_date
            movie.poster_path = poster_path
            movie.overview = overview
            movie.vote_average = vote_avereage
            movie.original_title = original_title
            movie.movie_id = movieid
            for i in range(len(genreItems)):
                for j in range(len(genreDatas)) :
                    if genreItems[i] == genreDatas[j]['id'] :
                        movie.genrename+=(genreDatas[j]['name']+ ' ')

            actorList = requests.get(actorUrl).json()
            actorDatas = actorList.get('cast')
           
            for i in range(4):
                try:
                    actor_name = actorDatas[i].get('name')
                    actor_id = actorDatas[i].get('id')
                    Actor.objects.get_or_create(
                        id = actor_id,
                        name = actor_name,
                    )
                    movie.actorname += (actorDatas[i]['name'] + ' ')
                except:
                    continue 
                
                movie.save()
    return Response(actorDatas)
            
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def movie(request) :
    if request.method == 'GET' :
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def takeGenre(request): 
    if request.method == 'GET':
        genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR'
        genreList = requests.get(genreURL).json()
        genreDatas = genreList.get('genres')
        for genreData in genreDatas:
            Genre.objects.get_or_create(
            id = genreData.get('id'),
            name = genreData.get('name'))
    return Response(genreDatas)

@api_view(['GET'])
@permission_classes([AllowAny])
def genre(request) :
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def recommned(request) :
    movie = Movie.objects.order_by('-vote_average')[:10]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def moviedetail(request, movie_pk) :
    movies = Movie.objects.filter(id=movie_pk)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)