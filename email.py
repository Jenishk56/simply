import re
import time

start_time = time.time()
def emailParser():
    result = open("email_simple_parser.txt", "a")
    with open("email_big.txt") as f:
        for line in f:
            line = line.strip()
            findEmail = re.findall(r'[\w\]+@[\w\.-]+\.[\w\.-]+', line)
            domains = []
            if findEmail:
                for email in findEmail:
                    emailSplit = email.split("@")
                    username = emailSplit[0]
                    domains.append(emailSplit[1])
                    line = line.replace(username, "nobody")

            # print(findEmail.group)
            result.write(line)

end_time = time.time()
emailParser()
print("Time Different is {}".format(end_time-start_time))