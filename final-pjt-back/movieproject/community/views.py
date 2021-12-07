import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
from rest_framework.permissions import AllowAny
from .models import Comment , Review, detailReview
from .serializers import ReviewSerializer, CommentSerializer, RankSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
import random
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def review_list_create(request) :
    
    if request.method == 'GET' :
        reviews = Review.objects.all().order_by('-pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST' :
        User = get_user_model()
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def review_detail_create(request, movie_pk) :

    if request.method == 'GET' :
        detailreview = detailReview.objects.filter(movie_id = movie_pk)
        serializer = RankSerializer(detailreview, many=True)
        return Response(serializer.data)

    if request.method == 'POST' :
        User = get_user_model()
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = RankSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=user, movie_id=movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET' :
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE' :
        review.delete()
        return Response({ 'id': review_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail_update_delete(request, detailreview_pk, movie_pk):
    review = get_object_or_404(detailReview, pk=detailreview_pk)

    if request.method == 'GET' :
        serializer = RankSerializer(review)
        return Response(serializer.data)
    
    if not request.user.detailreview_set.filter(pk=detailreview_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    
    elif request.method == 'PUT':
        serializer = RankSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE' :
        review.delete()
        return Response({ 'id': detailreview_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def create_comment(request, review_pk) :
    if request.method == 'GET' : 
        comments = Comment.objects.filter(review_id=review_pk).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def comment_list(request) :
    comments = Comment.objects.all().order_by('-pk')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, comment_pk, review_pk) :
    comment = get_object_or_404(Comment, pk=comment_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    elif request.method == 'DELETE' :
        comment.delete()
        return Response({ 'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)


    
@api_view(['GET'])
@permission_classes([AllowAny])
def recommend(request) :
    movielist = {}
    reviewcount = detailReview.objects.filter(Q(rank='4') | Q(rank='5')).values('movie_id').distinct().count()
    review = detailReview.objects.filter(Q(rank='4') | Q(rank='5')).values('movie_id').distinct()
    print(review[0])
    for i in range(reviewcount) :
        movie = Movie.objects.filter(id=review[i]['movie_id'])
        serializer = MovieSerializer(movie, many=True)
        movielist[i] = serializer.data
    return Response(movielist)

@permission_classes([AllowAny])
def average(request, movie_pk) :
    review1count = detailReview.objects.filter(rank='1', movie_id=movie_pk).count()
    review2count = detailReview.objects.filter(rank='2', movie_id=movie_pk).count()
    review3count = detailReview.objects.filter(rank='3', movie_id=movie_pk).count()
    review4count = detailReview.objects.filter(rank='4', movie_id=movie_pk).count()
    review5count = detailReview.objects.filter(rank='5', movie_id=movie_pk).count()
    sum = (review1count*1) + (review2count*2) + (review3count*3) + (review4count*4) + (review5count*5)
    count = review1count+review2count+review3count+review4count+review5count
    avg = round(sum/count,1)
    
    return HttpResponse(avg)

@api_view(['GET'])    
@permission_classes([AllowAny])
def recommend2(request, user_pk) :
    review = detailReview.objects.filter(~Q(user_id=user_pk),rank='5').order_by('?').distinct()[:8]
    serializer = RankSerializer(review,many=True)
    
    
    return Response(serializer.data)