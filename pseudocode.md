<!--
FOR LATER
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
-->