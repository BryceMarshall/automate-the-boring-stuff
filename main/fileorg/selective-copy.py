import os
import shutil
import sys, re


def main():
    args = sys.argv[1:]

    if len(args) != 3:
        raise IOError("Only three args")

    folder, target, ending = args
    folder = os.path.abspath(folder)
    target = os.path.abspath(target)
    pattern = re.compile("(.*)?%s$" % ending)

    for foldername, folders, files in os.walk(folder):
        for file in files:
            if pattern.search(file) is not None:
                shutil.copy(os.path.join(foldername, file), os.path.join(target, file))



if __name__ == "__main__":
    main()