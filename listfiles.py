from os import walk

mypath = 'test'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    for f in filenames:
        fd = open(dirpath+"/"+f)
        print(fd.readlines())

# print(f)