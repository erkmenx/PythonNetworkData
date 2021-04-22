import re

handle = open('datas.txt')
total=list()
for line in handle:
    lineclear = line.strip()
    print(lineclear)
    x=re.findall('[0-9]+', lineclear)
    total= total + x

print(total)
y=0
for x in total:
    x=int(x)
    y=y+x

print(y)
