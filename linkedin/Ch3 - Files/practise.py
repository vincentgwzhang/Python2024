import os
from os import walk

def file_info():
    count = 0
    for (dirpath, dirnames, filenames) in walk("./deps/"):
        for file in filenames:
            file_name, file_extension = os.path.splitext(file)
            if file_extension == '.txt':
                file_stats = os.stat(file)
                count = count + file_stats.st_size
    return count