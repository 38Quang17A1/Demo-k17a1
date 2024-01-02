#1
a = eval(input("Nhập gtri a:"))
tong=0
n=0
while True:
    if tong > a:
        break
    n=n+1
    tong=tong+n

print("Gia tri n tim duoc: ", n)
#2
a = eval(input("Nhập gtri a: "))
tong = 0
n = 0
while True:
    if tong > a:
        break
    n = n+1
    tong = tong + n**2

print("Gia tri n tim duoc: ", n)



#4
a = eval(input("Nhập gtri a: "))
tich = 1
n = 1
while True:
    if tich > a:
        break
    n = n+1
    tich = tich*n 
print("Gtri n tìm đc:",n)
