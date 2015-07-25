# -*- coding: utf-8 -*-
import re
from .containers import Playlist, Song

def get_from_file(path):
  with open(path) as f:
    lines = [line.rstrip('\n') for line in f]
    name = lines.pop(0)
    preprocess = lambda s: re.sub('\[.*?\]', '', s).strip()
    p = Playlist(name, [])
    for l in lines:
      parts = preprocess(l).split(' - ')
      if len(parts) is not 2:
        print("Incorrect format:")
        print(parts)
        exit()
      p.songs.append(Song(parts[0], None, parts[1]))

    return p
