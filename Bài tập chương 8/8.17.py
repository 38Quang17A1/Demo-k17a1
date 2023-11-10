# Hàm tính UCLN sử dụng thuật toán Euclid
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Hàm tính BCLN của a và b
def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm

# Yêu cầu người dùng nhập hai số nguyên a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm và in ra BCLN của a và b
lcm = find_lcm(a, b)
print("Bội chung lớn nhất của", a, "và", b, "là:", lcm)