from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    album_id = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title
    
class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Album(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name} - {self.release_date} - {self.rating}"