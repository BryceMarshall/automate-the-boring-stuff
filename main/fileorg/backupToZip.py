import zipfile, os

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipfilename):
            break;
        number+=1

    backup = zipfile.ZipFile(zipfilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print("Compressing files in {}".format(foldername))
        backup.write(foldername)
        for filename in filenames:
            newbase = os.path.basename(folder) + '_'
            if filename.startswith(newbase) and filename.endswith(".zip"):
                continue
            backup.write(os.path.join(foldername, filename))
    backup.close()
    print("Done.")

backupToZip(".")