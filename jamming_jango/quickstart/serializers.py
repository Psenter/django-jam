from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Artist, Genre, Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["type"]

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "release_date", "rating"]