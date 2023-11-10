
#Tính năm nhuận hay ko nhuận 
year= int(input("Nhập năm: "))
if ((year% 4 == 0) and (year% 100 !=0)) or (year% 400== 0):
    print("Đây là năm nhuận!")
else:
    print("Đây là năm không nhuận!")