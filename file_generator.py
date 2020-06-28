w = open("email_big.txt", "a")
count = 0
while count < 1000:
    w.write("Ryan has sent an invoice email to john.d@yahoo.com")
    w.write("by using his email id ryan.arjun@gmail.com and he also")
    w.write("shared a copy to his boss rosy.gray@amazon.co.uk on the cc part.")    
    count+=1



