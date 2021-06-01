"""
Parse input arguments and route downloads to necessary places
"""
import argparse
parser = argparse.ArgumentParser(description='Youtube downloader')

# Add the arguments
parser.add_argument(
    '-i', 
    '--input', 
    help="""
    The text file with youtube urls to be downloaded.
    Note: If there is no .txt file provided, a prompt will ask if you want to 
    download all .txt files in the current dir (and all sub dirs)
    """)
parser.add_argument(
    '-o', 
    '--output', 
    help="""
    The output directory to download the files to. 
    Note: If the directory doesn't exist, the app will create the directory. 
    If no path is supplied, the audio files will be downloaded in the current working dir
    """)
parser.add_argument(
    '-v',
    '--verbose',
    action = "store_true",
    default=False,
    help="Verbose logging"
)

args = parser.parse_args()
