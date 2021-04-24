###Adından da anlaşıldığı üzere javascript nesnesi gösterimi.

### Daha basit ve daha popülerdir.

### XML yerine kullanılabilir.


import json

data = '''{
"name" : "Chuck",
"phone": {
"type": "intl",
"number": "+905453555480"
},
"email": {
"hide": "yes"
}
} '''


info = json.loads(data)
print("Name:", info["name"])
print("Phone number:", info["phone"])
