Usage: spotify-crawler [OPTIONS] COMMAND [ARGS]...

  spotify-crawler <COMMAND> --help for specific info

Options:
  --help  Show this message and exit.

Commands:
  groovehack  Load tracks from groovehack set
  itunes      Load tracks from itunes.
  textfile    Load tracks from file into spotify playlist.

Example
spotify-crawler textfile ../playlist.txt 2>&1 >tmp

puts errors in stdout and resulting playlist(s) in tmp

