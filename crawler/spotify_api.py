import re
import click
import spotipy
import spotipy.util as util
import settings


class Spotify(object):
  def __init__(self, username=settings.USERNAME):
    super(Spotify, self).__init__()
    self.sp = spotipy.Spotify(auth=spotify_auth(username))
    self.username = username

  def create_playlists(self, ps):
    return [self.create_playlist(p) for p in ps]

  def create_playlist(self, p):
    track_uris = [self.search_track_uri(s) for s in p.songs]

    l_all = len(track_uris)
    track_uris = filter(None, track_uris)
    l = len(track_uris)
    diff = l_all-l
    if diff > 0:
      click.echo('found: %d songs (%d missing)' % (l, diff), err=True)

    playlist = self.get_or_create_playlist(p.name)
    self.sp.user_playlist_replace_tracks(self.username, playlist, track_uris)
    return playlist

  def search_track_uri(self, song, attempt=0):
    if attempt > 1:
      click.echo('FAILED: attempt: ' + str(attempt) + ' Song: ' + str(song), err=True)
      return None

    s = 'artist:'+ song.artist + ' track:'+ song.name
    s = re.sub('[Ff]eat. ', '', s)
    s = re.sub('[&,-]', '', s).strip()

    if attempt==0:
      s = re.sub('[()]', '', s)
    elif attempt==1:
      s = re.sub('\(.*?\)', '', s)

    result = self.sp.search(s, limit=1)
    items = result['tracks']['items']


    if len(items) == 0:
      # click.echo("QUERY: " + s)
      return self.search_track_uri(song, attempt+1)
    else:
      i = items[0]
      # click.echo("FOUND: " + i['artists'][0]['name'] + ' - ' +  i['name'] + "\n")
      return i['uri']

  def get_or_create_playlist(self, name):
    playlists = self.sp.user_playlists(self.username)
    for playlist in playlists['items']:
      if playlist['name'] == name:
        return playlist['uri']

    playlist = self.sp.user_playlist_create(self.username, name)
    return playlist['uri']


def spotify_auth(username):
  token = util.prompt_for_user_token(username, settings.SCOPE, client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET, redirect_uri=settings.REDIRECT_URI)
  if not token:
    click.echo("ERROR WITH TOKEN", err=True)
    exit(-1)
  return token
