import json
import urllib.request, urllib.parse, urllib.error


address= input("Enter Address:")

data = urllib.request.urlopen(address).read().decode()

info = json.loads(data)
info2= info['comments']
print('User count:', len(info2))
sum=0
for item in info2:
    print('Count', item['count'])
    sum=sum+int(item['count'])


print(sum)
