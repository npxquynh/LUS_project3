from os import listdir
from os.path import isfile, join

def list_all_files(folder_path):
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

    return files