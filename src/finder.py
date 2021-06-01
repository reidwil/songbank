"""
Finds .txt files in current dir and sub dirs
"""
import os

def files_to_download():
    PATH = os.getcwd()
    extention = '.txt'
    remove_items = PATH + '/requirements.txt'
    results = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames 
                if os.path.splitext(f)[1] == extention]
    return [x for x in results if x != remove_items]
