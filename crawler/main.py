# -*- coding: utf-8 -*-
import click
from .file_parser import get_from_file
from .itunes_parser import get_itunes_playlists
from .spotify_api import Spotify
from .groovehack_parser import get_groovehack_set

@click.group()
def cli():
  """spotify-crawler <COMMAND> --help for specific info"""
  pass


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--filter', help='Filter for playlists that match the regex')
@click.option('--show-only', is_flag=True, default=False, help='Do not import to spotify, just print em')
def itunes(file, filter, show_only):
  """Load tracks from itunes.\n
  Ex.: spotify-crawler itunes --filter '^cd-' Mediathek.xml"""

  ps = get_itunes_playlists(file, filter)
  if show_only:
    for p in ps:
      click.echo(p.name)
      for i, s in enumerate(p.songs):
        click.echo(str(i+1) + ' - ' + unicode(s))
      click.echo()
  else:
    get_playlists(ps)


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

@click.command()
@click.argument('url')
def groovehack(url):
  """
  Load tracks from groovehack set
  """
  p = get_groovehack_set(url)
  get_playlists([p])


def get_playlists(ps):
  s = Spotify()
  result = s.create_playlists(ps)
  click.echo(' '.join(result))

cli.add_command(itunes)
cli.add_command(groovehack)
cli.add_command(textfile)

if __name__ == '__main__':
    cli()
