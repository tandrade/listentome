import requests
from urllib.parse import urlencode, urlparse

from flask import current_app, render_template, request
from app import app


def generate_redirect_uri(request):
    parsed_uri = urlparse(request.url)
    return "{uri.scheme}://{uri.netloc}/authorization".format(uri=parsed_uri)

@app.route("/")
def main():
    login_params = {
        "client_id": current_app.config['CLIENT_ID'],
        "response_type": "code",
        "redirect_uri": generate_redirect_uri(request),
        "scope": "user-library-read"
    }
    spotify_url = "https://accounts.spotify.com/authorize?" + urlencode(login_params)
    return render_template("login.html", spotifylink=spotify_url)

@app.route("/authorization")
def authorization():
    if "code" not in request.args:
        return render_template("authorization_error.html")
    token = requests.post("https://accounts.spotify.com/api/token", data={
        "grant_type": "authorization_code",
        "code": request.args["code"],
        "redirect_uri": generate_redirect_uri(request),
        "client_id": current_app.config["CLIENT_ID"],
        "client_secret": current_app.config["CLIENT_SECRET"]
    })
    if not token.status_code == 200:
        return render_template("authorization_error.html")
    data = token.json()
    if "access_token" not in data:
        return render_template("authorization_error.html")

    song_data = requests.get()
    return render_template("authorize.html", code=token.json()["access_token"])
