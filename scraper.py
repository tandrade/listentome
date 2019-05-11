import requests

# TODO: is there an easier way to do this?
def parse_client_files(data):
    return data[0].replace("\n", "")

with open("clientsecret", "r") as f:
    clientsecret = parse_client_files(f.readlines())

with open("clientid", "r") as f:
    clientid = parse_client_files(f.readlines())

print(clientsecret)
print(clientid)

# saved tracks
saved_songs_endpoint = "https://api.spotify.com/v1/me/tracks"
# TODO: handle pagination
