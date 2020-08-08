import os

rootdir = os.getcwd()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        if file.endswith(".mp4"):
            if file[7] == '1' or file[7] == '2':
                os.remove(filepath)