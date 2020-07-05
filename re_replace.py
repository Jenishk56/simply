import re
stra = "hello i am here jenish@gmai.com"
stra = re.sub(r'[\w\]+@[\w\.-]+\.[\w\.-]+', '', stra)
# str.replace("hello", "12")
# print(str)