from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SongSerializer, ArtistSerializer, GenreSerializer, AlbumSerializer
from .models import Song, Artist, Genre, Album

#creates my class
class SongViewSet(viewsets.ModelViewSet):
    #gets all objects from the "Song" model
    queryset = Song.objects.all()
    #sets the serializer for this class
    serializer_class = SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer