import re     #### Regular expression import

### if line.find('From ')>=0 yerine if re.search('Find', line) kullanılabilir.


### if line.startswith('From ')>=0 yerine, if re.search('^Find ', line) kullanılır
### Burada ^F, F ile başlayan bir cümle demektir. ^ Cümlenin başındaki karakterdir.

### . karakteri tüm karakterlerle eşleşebilir
### * karakteri "0 or more" demektir. Beraber .* kullanınca aradaki karakterler farketmez demektir.


### X-Sieve: CMU Sieve 2.3      --->  ^X.*: olarak da aranabilir.

### "\S" tek başına bir karakterdir ve boşluk olmayan herhangi bir karakter demektir. \S+ one or more

### X-Dwqeqwe-SAdasdas-wwww:      ----> ^X-\S+: olarak da aranabilir.
