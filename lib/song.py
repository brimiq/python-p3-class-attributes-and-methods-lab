class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    # store raw values so histogram counting works
    _all_genres = []
    _all_artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # track total songs
        Song.add_song_to_count()

        # store raw duplicates
        Song._all_genres.append(genre)
        Song._all_artists.append(artist)

        # update unique lists
        Song.add_to_genres()
        Song.add_to_artists()

        # update histograms
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls._all_genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls._all_artists))

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}
        for genre in cls._all_genres:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}
        for artist in cls._all_artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
