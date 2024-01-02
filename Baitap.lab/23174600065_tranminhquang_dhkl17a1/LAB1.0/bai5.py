#ktra so chan
def so_chan(n):
    if n % 2 !=0:
        return False
    else:
        return True

n = int(input("Nhap so n: "))
if so_chan(n):
    print(n, "la so chan")
else:
    print(n, "khong la so chan")