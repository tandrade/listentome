from flask import render_template
from app import app

@app.route("/")
def main():
    return "Explore your music. Log in to Spotify."
