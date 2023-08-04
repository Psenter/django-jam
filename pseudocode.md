# MoSCoW

### Must have:
  * Use django rest framework to build API routes
  * Routes to preform CRUD operations for each table model
  * PostgreSQL database to store all of the tables
  * Routes to display the info as JSON

### Should have:
  * Filter lists by artist, album, or other ways
  * A way to search for a single song
  * Allow user to add songs to the database

### Could have:
  * Ways to have a user create a playlist and add songs to said playlist
  * A react frontend
  * Number of times a song has been played

### Won't have:
  * Spotify premium (you have to listen to 30 second ads all day)
  * Can't actually play any songs

# Models:
```
class Song(models.Model):
  title = models.Charfield()
  album_id = models.ForeignKey()
  artist_id = models.ForeignKey()

  def __str__(self):
        return self.Song

class Artist(models.Model):
  name = models.Charfield()

  def __str__(self):
        return self.Artist

class Genre(models.Model):
  type = models.Charfield()

  def __str__(self):
        return self.Genre

class Album(models.Model):
  name = models.Charfield()
  release_date = models.Charfield()
  rating = models.CharField()
  artist_id = models.ForeignKey()

  def __str__(self):
        return self.Album
```

# Views
```
def get_songs():
  queryset = Song.objects.all()
  serializer_class = SongSerializer

def get_artists():
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

def get_genre():
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

def get_albums():
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer
```

# Endpoints
```
/songs
/genre
/artist
/album
```

# DB schema
```
Table song {
  id integer [primary key]
  name varchar
  album_id fk
  artist_id fk
  genre manyToMany
}

Table artist {
  id integer [primary key]
  name varchar
}

Table genre {
  id integer [primary key]
  type varchar
}

Table album {
  id integer [primary key]
  name varchar
  release_date varchar
  rating varchar
  artist_id fk
}

Table song_genre {
  id integer [primary key]
  song_id fk
  genre_id fk
}

Ref: "song"."id" < "song_genre"."song_id"

Ref: "genre"."id" < "song_genre"."genre_id"

Ref: "artist"."id" < "song"."artist_id"

Ref: "artist"."id" < "album"."artist_id"

Ref: "album"."id" < "song"."album_id"
```