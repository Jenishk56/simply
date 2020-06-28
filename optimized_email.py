import re
import os
import io
import time
start_time = time.time()

def emailParse():
    bufsize = io.DEFAULT_BUFFER_SIZE
    result = open("email_optimized_parser.txt", "w")
    fsize = os.stat("email_big.txt").st_size
    with open("email_big.txt") as f:
        if bufsize > fsize:
            bufsize = fsize-1
        
        i = 0
        while i < fsize:
            if i != 0:
                counter = 0
                while f.seek(i) != ' ' and f.seek(i) != ',' and i > 0 and counter < 320:
                    i-=1
                    counter+=1

            f.seek(i)
            next_slot = i + bufsize
            while f.tell() < next_slot and f.tell() <= fsize:
                # data.append(f.readlines())
                line = f.readline(next_slot-f.tell())
                # print(line)
                line = line.strip()
                findEmail = re.findall(r'[\w\]+@[\w\.-]+\.[\w\.-]+', line)
                if findEmail:
                    for email in findEmail:
                        emailSplit = email.split("@")
                        username = emailSplit[0]
                        line = line.replace(username, "nobody")

                result.writelines(line)
                i += bufsize

end_time = time.time()
emailParse()
print("Time difference is {}".format(end_time-start_time))