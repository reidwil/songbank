import os
import sys
import re
import string
import pafy


def clean_title(title: str) -> str:
    cleaned = re.sub("[^a-zA-Z0-9_ ]", "", title)
    cleaned = re.sub("[ ]", "_", filename)
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
    # Operator for the .txt file
    with open(filename, "r") as urls:
        num_videos = 0
        for url in urls.read().split():
            try:
                get_audio(url, dl_dir)
                num_videos += 1
            except:
                print("Failed to download: {url}".format(url = url))
                pass
        print("Downloaded and converted %d video(s)" % num_videos)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dl_dir = os.getcwd()
        main(filename, dl_dir)
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        dl_dir = sys.argv[2]
        main(filename, dl_dir)
    else:
        print("Downloading Reid's files\n")
        cur_dir = os.getcwd()
        dl_dir = os.path.join(cur_dir, "/reids-songs")
        if not os.path.exists(dl_dir): os.mkdir(dl_dir) 
        for filename in os.listdir(cur_dir + "/backlog"):
            main("backlog/" + filename, dl_dir)
