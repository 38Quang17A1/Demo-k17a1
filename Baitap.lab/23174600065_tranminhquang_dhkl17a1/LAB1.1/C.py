#C = tinh tong cac so le tu 1 den n
n = int(input("Nhap so n: "))
tong = 0
for i in range(1,n+1):
    if n % i!=0:
        tong += i
print("tong cac so le tu 1 den", n, "la: ", tong)