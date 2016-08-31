import re

file = tuple(open('Chelsea vs Burnley.txt','r'))

events = []

for data in file:
    matchObj = re.match(r"(\d+)'([a-z]+\s*[a-z]*\s*[a-z]*).*\((\w+)\)", data)
    if matchObj:
       print(matchObj.group())
