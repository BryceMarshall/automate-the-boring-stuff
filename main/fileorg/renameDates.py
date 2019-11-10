import os, re, shutil

def main():

    USAPattern = re.compile(r'''
                    ^(.*?)
                    ((0|1)?\d)-
                    (([0-3])?\d)-
                    ((19|20)\d\d)
                    (.*?$)
    ''', re.VERBOSE)

    for file in os.listdir("."):
        print("Checking file %s" % file)
        fileMatch = USAPattern.search(file)
        if fileMatch is not None:
            print("Renaming file %s" % file)
            month, day, year = (fileMatch.group(2), fileMatch.group(4), fileMatch.group(6))
            newName = fileMatch.group(1) + '-'.join([day, month, year]) + fileMatch.group(8)
            origFile = os.path.abspath(file)
            dirName = os.path.dirname(origFile)
            shutil.move(origFile, os.path.join(dirName, newName))

main()