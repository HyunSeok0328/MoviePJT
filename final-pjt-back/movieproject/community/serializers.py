from rest_framework import serializers

from movies.serializers import MovieSerializer
from .models import Review, Comment, detailReview
from accounts.serializers import UserSerializer



class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'title','content','created_at','updated_at','user','user_id')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'review','created_at','updated_at','user','user_id')

class RankSerializer(serializers.ModelSerializer) :
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    class Meta :
        model = detailReview
        fields = ('id', 'rank', 'content','movie_id','user_id','user','movie')      