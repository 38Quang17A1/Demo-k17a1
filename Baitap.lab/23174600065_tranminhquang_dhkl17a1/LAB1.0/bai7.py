def so_doixung(n):
    return str(n) == str(n)[::-1]
n = int(input("Nhập số n: "))
if so_doixung(n):
    print(n,"là số đối xứng")
else:
    print(n, "không là số đối xứng")
    