
from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_movie_recommendations,name='get_movie_recommendations'),
]
