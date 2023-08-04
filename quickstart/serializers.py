from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Artist, Genre, Album

#defines my serializer class
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        #focuses on serializing the "Artist" model
        model = Artist
        #all fields of Artist will be included
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Song
        fields = '__all__'