# Khởi tạo biến tổng S
S = 0

while True:
    try:
        num = int(input("Nhập số nguyên (kết thúc là số 0): "))
        
        if num == 0:
            break  # Kết thúc vòng lặp nếu người dùng nhập 0
        
        S += num
    except ValueError:
        print("Lỗi: Không phải là số nguyên. Hãy thử lại.")

# In ra tổng S
print("Tổng các số nguyên bạn đã nhập là:", S)