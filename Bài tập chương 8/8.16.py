# Hàm tính UCLN sử dụng thuật toán Euclid
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Yêu cầu người dùng nhập hai số nguyên a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm và in ra UCLN của a và b
gcd = find_gcd(a, b)
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd)