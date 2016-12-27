import os


def find_dublicates(user_folder):
    # key = (name, size,)
    all_files = {}
    dublicates = set()
    for path, subdirs, files in os.walk(user_folder):
        for name in files:
            path_with_name = os.path.join(path, name)
            name_size = name, os.path.getsize(path_with_name)
            if name_size not in all_files:
                all_files[name_size] = path_with_name
            else:
                dublicates.add(all_files[name_size])
                dublicates.add(path_with_name)
    return sorted(dublicates)


if __name__ == '__main__':
    user_folder = input("Enter path to folder or press 'Enter' to scan "
                        "current folder and subfolders: ")
    if not user_folder:
        user_folder = os.getcwd()
    dublicates = find_dublicates(user_folder)
    if dublicates:
        print("Dublicates:")
        print(*dublicates, sep='\n')
    else:
        print('There are no dublicates')
