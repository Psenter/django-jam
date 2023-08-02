# MoSCoW

### Must have:
  * Use django rest framework to build API routes
  * Routes to preform CRUD operations for each table model
  * PostgreSQL database to store all of the tables
  * Routes to display the info as JSON

### Should have:
  * Filter lists by artist, album, or other ways
  * A way to search for a single song

### Could have:
  * Ways to have a user create a playlist and add songs to said playlist

### Won't have:
  * Spotify premium (you have to listen to 30 second ads all day)

# Questions:
  *

# Models:
```
class Song(models.Model):
  title = models.Charfield()
  album_id = models.ForeignKey()

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

  def __str__(self):
        return self.Album
```

# Views
```
def get_all(request):
  //find a way to get all the tables to display

def get_songs():
  //only display songs

def get_artists():
  //only display the artists

def get_genre():
  //only display the genres

def get_albums():
  //only display the albums
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
  album_id integer
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
}

Table artist_songs {
  id integer [primary key]
  song_id fk
  artist_id fk
}

Table artist_albums {
  id integer [primary key]
  artist_id fk
  album_id fk
}

Table song_genre {
  id integer [primary key]
  song_id fk
  genre_id fk
}

Ref: "artist"."id" < "artist_songs"."artist_id"

Ref: "song"."id" < "artist_songs"."song_id"

Ref: "album"."id" < "artist_albums"."album_id"

Ref: "artist"."id" < "artist_albums"."id"

Ref: "song"."id" < "song_genre"."song_id"

Ref: "genre"."id" < "song_genre"."genre_id"
```