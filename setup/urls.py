"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Function Based view
# from genres.views import genre_create_list_view, genre_detail_view
#Class based view
from genres.views import GenreCreateListView, GenreRetrieveUpdadeDestroy
from actors.views import ActorCreateListView, ActorRetrieveUpdadeDestroy
from movies.views import MovieCreateListView, MovieRetrieveUpdadeDestroy



urlpatterns = [
    path('admin/', admin.site.urls),

    #Function based view
    #path('genres/', genre_create_list_view, name='genre-create-list'),
    #Class based view
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),

    #Function based view
    #path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view'),
    #Class based view
    path('genres/<int:pk>/', GenreRetrieveUpdadeDestroy.as_view(), name='genre-detail-view'),
    path('actors/<int:pk>/', ActorRetrieveUpdadeDestroy.as_view(), name='actor-detail-view'),
    path('movies/<int:pk>/', MovieRetrieveUpdadeDestroy.as_view(), name='movie-detail-view'),
]   
