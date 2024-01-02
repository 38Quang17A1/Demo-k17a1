n = int(input("Nhập số nguyên dương n: "))

print("cac uoc so cua", n, "la:", end=",")
tong_uoc = 0
so_uoc = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        tong_uoc += i
        so_uoc += 1

print("so luong uoc cua", n, "la: ", so_uoc)
print("tong cac uoc so cua", n, "la: ", tong_uoc)