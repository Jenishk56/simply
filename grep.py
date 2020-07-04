import re
file = open("grep_sample.txt", "w")
# Write a file to search

file.write("first line\nsecond line\nthird line")
file.close()

pattern = "second"
# Search pattern


file = open("grep_sample.txt", "r")
for line in file:
    if re.search(pattern, line):
        print(line)