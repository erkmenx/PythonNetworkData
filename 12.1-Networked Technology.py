#### Bu 3 satır kod ile telefon çalma işlemi yapılabilir.s


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x= mysock.connect(('data.pr4e.org', 80))

print(x)
