from db.run_sql import run_sql
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (album_title, album_genre) VALUES (%s, %s,"