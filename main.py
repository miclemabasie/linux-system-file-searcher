import os
import time
import fnmatch

def find_files(directory, pattern):
    """
    Takes a directory and file pattern as parameter and searches
    the entire dir for the file matching that pattern.
    """
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(root, filename)


def main():
    directory = input("Enter the path to the folder you wish to search: ")
    pattern = input("Enter the file pattern: ")
    find_files(directory, pattern)
    for file in find_files(directory, pattern):
        time.sleep(1)
        print(file)

if __name__ == "__main__":
    main()