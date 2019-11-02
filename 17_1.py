# Implement a simple Audio Streaming Service class architecture
# It'll include 3 classes - Song, Album and Artist
#
# Artist class:
#   - name: str
#   - country: str
#   - songs: list = []
#   - albums: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - albums_number: int - must be declared using property decorator as the
#   length of albums list
#
# Album class:
#   - name: str
#   - year: int
#   - genre: str
#   - artist: Artist
#   - songs: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - duration: float - must be declared using property decorator. Album
#   duration is the sum of all songs' (from songs list) duration.
#
# Song class:
#   - name: str
#   - artist: Artist
#   - features: list[Author] = [] (can feature 1 or more Artists)
#   - year: int
#   - duration: float
#   - album: Album (can be None if it's a single)
#
#   when you specify an album, make sure add the song to album's [songs] list.
#   the same with Arist albums/songs lists
#
#   Also, you need implement a custom exception WrongArtistError which is
#   raised when you try to add a song to an album and artists don't match.


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.songs = set()
        self.albums = set()

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def albums_number(self):
        return len(self.albums)

    def __repr__(self):
        return self.name


class Album:
    def __init__(self, name, year, genre, artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = set()
        artist.albums.add(self)

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return sum(song.duration for song in self.songs)

    def add_song(self, song):
        if song.artist != self.artist:
            raise WrongArtistError("the artist doesn't match the album")
        else:
            self.songs.add(song)

    def __repr__(self):
        return self.name


class Song:
    def __init__(self, name, artist, features, year, duration, album):
        self.name = name
        self.artist = artist
        self.features = features
        self.year = year
        self.duration = duration
        self.album = album
        album.add_song(self)
        artist.songs.add(self)

    def __repr__(self):
        return self.name

