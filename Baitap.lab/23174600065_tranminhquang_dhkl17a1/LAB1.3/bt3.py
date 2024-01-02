chuoi_so = input("Nhập dãy số cách nhau bằng khoảng trắng: ")
danh_sach_so = chuoi_so.split()
danh_sach_so = [int(so) for so in danh_sach_so]

so_le = []
so_chan = []

for so in danh_sach_so[::-1]:
    if so % 2 == 0:
        so_chan.append(so)
    else:
        so_le.append(so)

ket_qua = so_le + so_chan  # Ghép số lẻ và số chẵn lại với nhau

print("Dãy số sau khi đảo ngược và chỉ hiển thị số lẻ/chẵn là:")
for so in ket_qua:
    print(so, end=" ")