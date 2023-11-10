n = int(input("Nhập số lượng số lẻ : "))

# Tạo một danh sách số ban đầu bắt đầu từ 1
sequence = [i for i in range(1, 2 * n, 2)]

# Đảo ngược danh sách
reversed_sequence = list(reversed(sequence))

# In ra dãy số lẻ sau khi đảo ngược
print("Dãy số lẻ sau khi đảo ngược:", reversed_sequence)