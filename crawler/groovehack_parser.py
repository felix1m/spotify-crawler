from __future__ import print_function
try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    from urllib import urlopen
import pprint
import json
from containers import Playlist, Song

API_SEARCH_URI = "http://www.groovehack.com/api/sets?glob="

def get_groovehack_set(url):
  parse_object = urlparse(url)
  slashparts = parse_object.path.split('/')
  playlist_glob = slashparts[-1]

  socket = urlopen(API_SEARCH_URI+playlist_glob)
  data = json.load(socket)

  tracks = filter(None, map(parse_track, data['tracks']))
  return Playlist(data['name'], tracks)

def parse_track(track):
  artist = track['artist']
  title = track['title']
  if artist == "UNKNOWN":
    return None
  else:
    return Song(str(artist), None, str(title))
