import re
import sys
import shutil
import os

def applyRegex(filename, regex : re.Pattern):
    infile = open(filename, "r")
    return [":".join(str(elem) for elem in [filename, lineNumber, line])
            for lineNumber, line in enumerate(infile.readlines())
            if regex.search(line) is not None]
    # result = []
    # for lineNumber, line in enumerate(infile.readlines()):
    #     if regex.search(line) is not None:
    #         print("Regex search : {}".format(regex.search(line)))
    #         result.append(":".join(str(elem) for elem in [filename, lineNumber, line]))
    # return result;

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        raise IOError("Two args only")

    path = args[0]
    regex = args[1]


    if not os.path.isabs(path):
        path = os.path.abspath(path)

    pattern = re.compile(regex)

    result = []

    for entry in os.walk(path):
        files = entry[2]
        for file in files:
            if (file.endswith(".txt")):
                result += applyRegex(os.path.join(entry[0], file), pattern)

    return result

main()