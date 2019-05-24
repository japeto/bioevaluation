import glob
files_words = glob.glob("./*.txt")
print(files_words)
for file in files_words:
    lines = ""
    try:
        for line in open(file, "r"):
            lines = lines +line.split("\t")[2]
        # print(lines)
        file = open(file, "w")
        file.write(lines)
        file.save()
    except:
        pass