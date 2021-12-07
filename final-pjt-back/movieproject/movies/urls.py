from django.urls import path
from . import views


urlpatterns = [
    path('', views.takeMovie),
    path('home/', views.movie),
    path('takegenres/',views.takeGenre),
    path('genre/', views.genre),
    path('recommend/', views.recommned),
    path('<int:movie_pk>/', views.moviedetail)
]