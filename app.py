import os
import sys
from src.downloader import main
from src.parser import args
from src.finder import files_to_download

# Set download dir if not supplied
if args.output is None:
    if args.verbose: 
        print(f"You didn't supply the output dir (-o/--output). the audio files will write here: {os.getcwd()}")
    args.output = os.getcwd()

if __name__ == "__main__":
    # print(args.input, args.output)
    if args.input is None:
        if args.verbose:
            print(f"No input file was provided, searching for all .txt files starting with {os.getcwd()}")
        files = files_to_download()
        if len(files) < 1:
            print("Found 0 .txt files.\nExiting")
            sys.exit()
        print("Found these .txt files:")
        print(*files, sep = '\n')
        should_download_all = input("Should download all? (y/n)")
        if should_download_all == 'y':
            [main(x, args.output) for x in files]
        elif should_download_all == 'n':
            args.input = input("Please specify one of the above files to download: ")
            if args.input in files:
                print(f"Found {args.input} - downloading now")
                main(args.input, args.output)
            else: 
                print(f"Provided incorrect .txt file. (Hint: copy and paste one of the above .txt files)")
                sys.exit()
        else: 
            print("Didn't provide `y` or `n`\nExiting")
            sys.exit()
    else:
        if not os.path.exists(args.output): os.mkdir(args.output) 
        main(args.input, args.output)
    # if len() == 2:
    #     filename = sys.argv[1]
    #     dl_dir = os.getcwd()
    #     main(filename, dl_dir)
    # elif len(sys.argv) == 3:
    #     filename = sys.argv[1]
    #     dl_dir = sys.argv[2]
    #     main(filename, dl_dir)
    # else:
    #     print("Downloading Reid's files\n")
    #     cur_dir = os.getcwd()
    #     dl_dir = os.path.join(cur_dir, "./reids-songs")
    #     if not os.path.exists(dl_dir): os.mkdir(dl_dir) 
    #     for filename in os.listdir(cur_dir + "/backlog"):
    #         main("backlog/" + filename, dl_dir)