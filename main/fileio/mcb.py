#!venv/bin/python

import sys
import shelve

import pyperclip


def main():
    args = sys.argv[1:]

    shelf = shelve.open("mcb-shelf")

    if len(args) > 2:
        raise IOError("max two args")
    if len(args) == 2:
        if args[0].lower() == "save":
            shelf[args[1]] = pyperclip.paste()
        if args[0].lower() == 'delete':
            del shelf[args[1]]
    if (len(args) == 1):
        if args[0].lower() == "list":
            pyperclip.copy(str(list(shelf.keys())))
        if args[0].lower() == 'delete':
            for k in shelf.keys():
                shelf.pop(k, None)
        if shelf[args[0]]:
            pyperclip.copy(shelf[args[0]])

if __name__ == "__main__":
    main()