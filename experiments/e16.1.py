import glob

myfiles = glob.glob("../files/*.txt")
for filepath in myfiles:
    print(filepath)