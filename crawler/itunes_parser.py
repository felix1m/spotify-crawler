from pyItunes import *
import re
from containers import *

def get_itunes_playlists(lib_path, regex):
  l = Library(lib_path)
  ps = l.getPlaylistNames()
  if regex:
    ps = filter(lambda k: re.match(regex, k), ps)
  return [parse_itunes_playlist(l, p) for p in ps]

def parse_itunes_playlist(l, p):
  songs = [Song(song.artist, song.album, song.name) for song in l.getPlaylist(p).tracks]
  return Playlist(p, songs)
