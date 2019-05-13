from flask_restful import abort, Resource


class SongCategorizer:

    def __init__(self, songs_metadata):
         self.energetic = []
         self.talkative = []

    def by_energy(self, n, reverse=False):
        return sorted(self.energetic, reverse=reverse)[:n+1]

    def by_talkative(self, n, reverse=False):
        return sorted(self.talkative, reverse=reverse)[:n+1]


class SongMetadata(Resource):

    def fetch_songs(self):
        # TODO: fetch songs from user library
        return {}

    def fetch_song_info(self):
        # TODO: iterate over chunks of code and fetch song info
        return {}

    def get(self):
        if "code" not in request.data:
            abort(400, message="A code is required to fetch song information.")
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
