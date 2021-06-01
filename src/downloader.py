import os
import sys
import re
import pafy
from src.tag import set_metadata


def clean_title(title: str) -> str:
    cleaned = re.sub("[^a-zA-Z0-9_ ]", "", title)
    cleaned = re.sub("[ ]", "_", cleaned)
    return cleaned

def get_audio(url: str, dl_dir: str):
    """ Pafy: https://pythonhosted.org/Pafy/ """
    audio = pafy.new(url)
    audio_stream = audio.getbestaudio(preftype="m4a", ftypestrict=True)
    filename = clean_title(audio.title)
    print('Downloading ', filename)
    filepath = os.path.join(dl_dir, filename + ".m4a")
    audio_output = audio_stream.download(filepath=filepath)
    return filepath, filename

def main(filename, dl_dir):
    with open(filename, "r") as urls:
        num_videos = 0
        for url in urls.read().split():
            try:
                fp, fn = get_audio(url, dl_dir)
                set_metadata(fp, fn)
                num_videos += 1
            except:
                print("Failed to download: {url}".format(url = url))
                pass
        print("Downloaded and converted %d video(s)" % num_videos)
