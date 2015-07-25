# songs: local
# tracks: spotify
class Song(object):
  """container for local song info"""
  def __init__(self, artist, album, name):
    super(Song, self).__init__()
    self.artist = artist
    self.album = album
    self.name = name

  def __str__(self):
    return ' - '.join(filter(None, [self.artist, self.name]))

# local
class Playlist(object):
  """local playlist container"""
  def __init__(self, name, songs):
    super(Playlist, self).__init__()
    self.name = name
    self.songs = songs

  def __str__(self):
    return 'Playlist :: "' + self.name + '"'
