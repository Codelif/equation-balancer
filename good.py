from pprint import pprint
from json import loads


f = open("jsonelem.txt")
a = []
d = loads(f.read())
for i in d.items():
    for elem in i[1]:
        a.append(elem["symbol"])
p = open("elements.txt", "w+")
for i in a:
    p.write(i+"\n")
p.close()