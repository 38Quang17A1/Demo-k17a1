#ktra so le
def so_le(n):
    if n % 2 ==0:
        return False
    else:
        return True

n = int(input("Nhap so n: "))
if so_le(n):
    print(n, "la so le")
else:
    print(n, "khong la so le")