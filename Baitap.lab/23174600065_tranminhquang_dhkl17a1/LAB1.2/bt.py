# tim 1 so nguyen duong nho nhat 1 +2 +3 +... +n>A
n = eval(input("nhap so n :"))
m = eval(input("nhap so A:"))
sum = 0
for i in range(1, 1000):
    if sum > m:
        break
    sum += i
print (i)
# tim 1 so nguyen duong nho nhat 1 +2^2 +.. + n^2 >A
a = eval(input("nhap so a:"))
tong = 0
n = 0 
while True:
    if tong > a:
        break
    n = n+1 
    tong = tong +n**2

print("gia tri n tim duoc", tong)
# tim so nguyen duong lon nhat 1 +2+...+n<A
n = eval(input("nhap so n :"))
m = eval(input("nhap so A:"))
sum = 0
for i in range(1, 1000):
    if sum < m:
        break
    sum += i
print (i)


# tim 1 so nguyen duong nho nhat 1 +2 +3 +... +n>A
n = eval(input("nhap so n :"))
m = eval(input("nhap so A:"))
sum = 0
for i in range(1, 1000):
    if sum > m:
        break
    sum += i
print (i)
# tim 1 so nguyen duong nho nhat 1 +2^2 +.. + n^2 >A
a = eval(input("nhap so a:"))
tong = 0
n = 0 
while True:
    if tong > a:
        break
    n = n+1 
    tong = tong +n**2

print("gia tri n tim duoc", tong)
# tim so nguyen duong lon nhat 1 +2+...+n<A
n = eval(input("nhap so n :"))
m = eval(input("nhap so A:"))
sum = 0
for i in range(1, 1000):
    if sum < m:
        break
    sum += i
print (i)