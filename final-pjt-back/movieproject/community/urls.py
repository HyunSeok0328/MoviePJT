from django.urls import path
from . import views



urlpatterns = [
    path('review/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('review/<int:review_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/review/', views.review_detail_create),
    path('<int:movie_pk>/review/<int:detailreview_pk>/', views.review_detail_update_delete),
    path('recommend/',views.recommend),
    path('review/<int:review_pk>/comments/<int:comment_pk>/', views.comment_delete),
    path('<int:movie_pk>/avg/', views.average),
    path('review/commentlist/', views.comment_list),
    path('<int:user_pk>/recommend2/',views.recommend2),
]