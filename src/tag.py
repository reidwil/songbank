import re
from mutagen import File

def split_file(filename):
    cleaned_name = re.sub('[^a-zA-Z0-9 \n\_\.]', '', filename)
    pair = cleaned_name.split("__")
    if len(pair) == 2:
        artist = str(pair[0]).replace('_', ' ')
        title = str(pair[1]).replace('_', ' ')
    else:
        artist = None
        title = str(pair[0]).replace('_', ' ')
    return artist, title

def set_metadata(filepath, filename):
    artist, title = split_file(filename)
    song = File(filepath, easy=True)
    song.add_tags()
    song.tags['artist'] = artist
    song.tags['title'] = title
    song.save()
    print(song.pprint())