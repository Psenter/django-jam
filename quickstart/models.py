from django.db import models

#creates song class
#adds fields "title", "album_id", "artist_id", and "genre"
#title is a character field
#album and artist id are both foreignkeys to make relationships with other tables
#genre is a many to many field that makes a pivot table
class Song(models.Model):
    title = models.CharField(max_length=200)
    album_id = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

#creates artist class with field name
class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
#creates genre class with field type
class Genre(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

#creates album class
#adds fields "name", "release_date", "rating", and "artist_id"
class Album(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    artist_id = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name} - {self.release_date} - {self.rating}"