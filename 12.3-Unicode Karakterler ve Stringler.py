####

print(ord('H'))     #### ASCII 0-256 arasındaki kodunu gösteriyor.
                    #### 8 bitlik hafıza byte olarak adlandırılır. Her karakter 1byte'dır.

print(ord('\n'))



##### Python 2.7.10 da x=u'Japonca' ve type(x) yazınca unicode çıkar iken
#### Python 3te x=u'Japonca' ve type(x) yazınca unicode değil string çıkar

### Çünkü python3'te bütün stringler Unicode'dur


while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    mystring = data.decode()            #### Decode çözümleme, encode şifreleme demek.
    print(mystring)                     #### Bu while döngüsü mysocka gelen bilgileri encodelayıp printliyor.
                                        #### UTF-8 de olabilir, ASCII'de
