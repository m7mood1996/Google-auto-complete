
import os

def get_files_path(diricory_path : str):
    txt_file = []
    dir_file = []
    for path in os.listdir(diricory_path):
        if path == ".DS_Store":
            continue
        full_path = os.path.join(diricory_path, path)
        if os.path.isfile(full_path):
            txt_file.append(full_path)
        elif os.path.isdir(os.path.join(diricory_path,path)):
            dir_file.append(os.path.join(diricory_path, path))
    if len(dir_file) == 0:
        return txt_file
    else:
        for dirictory in dir_file:
            txt = get_files_path(dirictory)
            txt_file += txt
    return txt_file