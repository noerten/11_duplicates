from collections import defaultdict
import os


def get_all_files(user_folder):
    all_files = defaultdict(list)
    for path, subdirs, files in os.walk(user_folder):
        for name in files:
            if not name.endswith('.py'):
                continue
            path_with_name = os.path.join(path, name)
            name_size = name, os.path.getsize(path_with_name)
            all_files[name_size].append(path_with_name)
    return all_files


def get_dublicates(all_files):
    dublicates = []
    for unique_item in all_files:
        if len(all_files[unique_item]) > 1:
            dublicates.extend(all_files[unique_item])
    return dublicates
               

if __name__ == '__main__':
    user_folder = input("Enter path to folder or press 'Enter' to scan "
                        "current folder and subfolders: ")
    if not user_folder:
        user_folder = os.getcwd()
    all_files = get_all_files(user_folder)
    dublicates = get_dublicates(all_files)
    if dublicates:
        print("Dublicates:")
        print(*dublicates, sep='\n')
    else:
        print('There are no dublicates')
