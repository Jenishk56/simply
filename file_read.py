# with open('/Users/jkhunt/numbers.txt') as f:
#     lines = f.read().splitlines()
# print(lines)

# with open('/Users/jkhunt/numbers.txt') as f:
#     for line in f:
#         print(line)

# with open('/Users/jkhunt/numbers.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         with open('/Users/jkhunt/numbers.txt', 'a') as w:
#             w.write(line)

import re
count = 0
result = open("email_result.txt", "a")

with open("email.txt") as f:
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



# count += len(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", st))


print(domains)
# print("email count is {}".format(count))

st = "my ip is 10.12.122.50 and 10.12.122.51 and 10.12.122.52 10.12.122.50 10.12.122.52"

result = {}

# grep -Eiorh '([[:alnum:]_.-]+@[[:alnum:]_.-]+?\.[[:alpha:].]{2,6})' "$@" * | sort | uniq > emails.txt

# with open("/home/facebook/test.log") as f:
#     for line in f:
#         line = line.strip()
#         colums = line.split(" ")
#         ip = colums[3]
#         if ip not in result:
#             result[ip] = 1
#         else:
#             result[ip] += 1

# for i in range(ip_count, -1, -1):
result = sorted(result.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

counter = 10
for value in result:
    if counter > 0:
        print(value)
    counter -= 1
print(result)
print("ip count is {}".format(count))


# generate minesweeper
# import random
# def generateBoard():
#     width = 3
#     height = 2
#     board = [[0 for x in range(width)] for y in range(height)]
#     mine_to_place = 3
#     mine_placed = 0
#     while (mine_placed < mine_to_place):
#         x = random.randrange(height)
#         y = random.randrange(width)
#         if board[x][y] != '*':
#             board[x][y] = '*'
#             mine_placed += 1
    
#     return board

# print(generateBoard())