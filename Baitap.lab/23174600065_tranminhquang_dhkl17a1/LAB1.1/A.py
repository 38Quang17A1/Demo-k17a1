#A = 1+2+3+...+n
n = int(input("Nhap so n: "))
tong=0
for i in range(1,n+1):
    tong += i
ket_qua = tong
print("tong cac so tu 1 den", n, "la: ", ket_qua)