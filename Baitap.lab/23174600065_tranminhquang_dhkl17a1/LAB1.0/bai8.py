#số harshad là số cha hết cho tổng các chữ số của nó
def so_harshad(so):
    tong_chu_so=0
    so_ban_dau = so
    while so >0:
        chu_so = so % 10
        tong_chu_so= tong_chu_so + chu_so
        so //=10

    return so_ban_dau % tong_chu_so == 0
so_can_kiem_tra = int(input("Nhập số cần kiểm tra: "))
if so_harshad(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số Harshad")
else:
    print(f"{so_can_kiem_tra} không phải là số Harshad")