from rest_framework import serializers
from .models import Movie,Genre


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id','title','release_date','poster_path','overview','vote_average','original_title','genres','genrename','movie_id','actorname')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)