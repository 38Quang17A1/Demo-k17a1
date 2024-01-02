def ktra_so_nguyen_to(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
n = int(input("Nhap so n: "))
if ktra_so_nguyen_to(n):
    print(n,"la so nguyen to")
else:
    print(n,"khong la so nguyen to")