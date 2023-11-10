#7.7 đổi tiền
so_tien_muon_doi = float(input("Số tiền muốn đổi :"))
so_to_1 = so_tien_muon_doi // 500000
tien_con_lai = so_tien_muon_doi%500000
print('Số tờ 500,000 :', so_to_1)
so_to_2 = tien_con_lai//200000
tien_con_lai = tien_con_lai%200000
print('Số tờ 200,000 :', so_to_2)
so_to_3 = tien_con_lai//100000
tien_con_lai = tien_con_lai%100000
print('Số tờ 100,000 :',so_to_3)
so_to_4 = tien_con_lai//50000
tien_con_lai = tien_con_lai%50000
print('Số tờ 50,000 :', so_to_4)
tien_con_lai = tien_con_lai*1
print('Tiền còn lại :', tien_con_lai)