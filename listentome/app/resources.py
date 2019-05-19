class SongMetadataCollectionException(Exception):
    pass


class SongCategorizer:

    def __init__(self, songs_metadata):
         self.energetic = []
         self.talkative = []

    def by_energy(self, n, reverse=False):
        return sorted(self.energetic, reverse=reverse)[:n+1]

    def by_talkative(self, n, reverse=False):
        return sorted(self.talkative, reverse=reverse)[:n+1]


class SongMetadataCollector(Resource):

    def __init__(self, code):
        self.code = code
        self.songs = []

    def fetch_songs(self):
        limit = 50
        offset = 0
        iterations = 0
        max_iterations = 50
        songs = requests.get("https://api.spotify.com/v1/me/tracks", params={"limit": limit}, headers={"Authorization": "Bearer %s" %})
        if songs.response_code != 200:
            raise SongMetadataCollectionException
        song_data = songs.json()
        offset = len(song_data["items"])

        count = song_data.get("count", 0)
        while limit * offset < count:
            iterations += 1
            songs = requests.get("https://api.spotify.com/v1/me/tracks", params={"limit": limit, "offset": offset}, headers={"Authorization": "Bearer %s" %})\
            if songs.response_code != 200:
                break
            song_data = songs.json()
            offset = offset  len(song_data["items"])
            if iterations >= max_iterations:
                break
        return []

    def fetch_song_info(self):
        # TODO: iterate over chunks of code and fetch song info
        return {}

    def get(self):
        n_songs = 15 # TODO: add query param
        songs = self.fetch_songs(code)
        song_info = self.fetch_song_info(songs)

        ranked = SongCategorizer(song_info)

        return {
            "energetic": {
                "top": ranked.by_energy(n_songs),
                "bottom": ranked.by_energy(n_songs, reverse=True)
            },
            "talkative": {
                "top": ranked.by_energy(n_songs),
                "bottom": ranked.by_energy(n_songs, reverse=True)
            }
        }
