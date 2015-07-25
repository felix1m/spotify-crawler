import click
from file_parser import get_from_file
from itunes_parser import get_itunes_playlists
from spotify_api import Spotify

@click.group()
def cli():
  """type spotify-crawler <COMMAND> --help for specific info"""
  pass


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--filter', help='Filter for playlists that match the regex')
def itunes(file, filter):
  """Load tracks from itunes.\n
  Ex.: spotify-crawler itunes --filter '^cd-' ../Mediathek.xml"""

  ps = get_itunes_playlists(file, filter)



@click.command()
@click.argument('file', type=click.Path(exists=True))
def textfile(file):
  """
  Load tracks from file into spotify playlist.\n
  Ex.: spotify-crawler textfile ../playlist.txt\n
  Format: (no blank lines)\n
  PLAYLIST_TITLE\n
  artist1 - song1\n
  artist2 - song2
  """
  p = get_from_file(file)
  get_playlists([p])


def get_playlists(ps):
  s = Spotify()
  result = s.create_playlists(ps)
  click.echo(' '.join(result))


cli.add_command(itunes)
cli.add_command(textfile)

if __name__ == '__main__':
    cli()
