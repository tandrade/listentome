from urllib.parse import urlencode, urljoin

from flask import current_app, render_template
from app import app

@app.route("/")
def main():
    redirect_uri = urljoin("http://" + current_app.config['BASE_URL'], "authorization")
    login_params = {
        "client_id": current_app.config['CLIENT_ID'],
        "response_type": "token",
        "redirect_uri": redirect_uri,
    }
    spotify_url = "https://accounts.spotify.com/authorize?" + urlencode(login_params)
    return render_template("login.html", spotifylink=spotify_url)

@app.route("/authorization")
def authorization():
    return render_template("authorize.html")
