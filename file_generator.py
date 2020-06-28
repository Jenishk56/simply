import random
w = open("random_big.txt", "w")
count = 0
dic = ["Hello World", "%", "Nice%", "Nanana", "1212121", "I am not gonna tell you how this is going work", "bhad me jao"]
while count < 100000:
    w.write(random.choice(dic))    
    w.write("\n")
    count+=1



