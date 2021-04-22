### re.search('', ) true/false geri bildirimi yapar.

### eğer eşleşen stringi çıkartmak istiyorsak re.findall() kullanılır.
import re
### Örneğin:

yazi = 'En sevdiğim 20 numara 8 ve 7dir'
goster = re.findall('[0-9]+', yazi)
print(goster)


### Başka bir kullanım şekli olarak büyük harf aratımı ve çıkarımı yapılabilir:

goster2 = re.findall('[EASDBCD]+', yazi)  #### A E C B M karakterlerini ayrı ayrı arattı.

print(goster2)



### GREEDY MATCHING

### + ve * karakterleri bu aramayı son bulabildikleri karaktere kadar yaparlar.


yazi2 = 'From: abdalerko: 23'

goster3 = re.findall('^F.+:', yazi2)
print(goster3)                                  ### Görüldüğü üzere son :'a kadar aldı.

## Çözümü ise * ya da -den önce ? koymaktır.

goster4 = re.findall('^F.+?:', yazi2)
print(goster4)



### Mesela Email bulalım.

yazi3= 'From muhammederkmen@gmail.com 09:05:10 10 March 2021'
goster5 = re.findall('\S+@\S+', yazi3)         ### \S+ @ \S+
print(goster5)


## Görüldüğü üzere çok rahat bir şekilde e maili çektik.

### Emailin hostunu bulalım:

konum= yazi3.find('@')
konum2= yazi3.find(' ', konum)
goster6=yazi3[konum+1:konum2]
print(goster6)


### Başka bir yöntem ile, double split yöntemi ile bulursak ise:

kelimeler=yazi3.split()
kisi=kelimeler[1]
parcala = kisi.split('@')
print('Maili atan kisi:',parcala[0])
print(parcala[1])


### Regular expressions ile bulma


kolayyol=re.findall('@([^ ]*)', yazi3)              ### [^ ]: Boşluk ile başlamayan kelimeler.
                                                    ### Buradaki ^ NOT ifadesini gösterir.
                                                    ### () içine çıkartılmak istenen ifade konur.
print(kolayyol)



### Escape Karakteri: örneğin $ karakterini aramak istiyoruz
### $ özel bir karakterdir ve aramak için başına \ konur. \$ şeklinde aratılır.

##### https://docs.python.org/3/howto/regex.html
