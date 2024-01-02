#A
n=eval(input("Nhập n:"))
tong=0
for i in range(1, n+1):
    tong+=i
print(tong)

#B
n=eval(input("Nhập n:"))
tong=0
for i in range(1, n+1):
    if i%2==0:
        tong==i
print(tong)

#C
n=eval(input("Nhập n:"))
tong=0
for i in range(1, n+1):
    if i%2!=0:
       tong+=i
print(tong)

#D
n=eval(input("Nhập n:"))
tich=1
for i in range(1, n+1):
    tich*=i
print(tich)

#H
import math
n=eval(input("Nhập n:"))
tong=0
for i in range(1,n+1):
    tong+=math.sqrt(i)
print(tong)


#G
n=eval(input("Nhập n:"))
tong=0
for i in range(1,n+1):
    tong+=(-1)**(i+1)/i
print(tong)