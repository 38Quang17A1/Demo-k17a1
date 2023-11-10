
#Tính tiền điện 
n=sokWh=int(input("Nhập số kWh:"))
sotien=0
if(n<=50):
    sotien=n*1678
elif(n<=100):
    sotien=50*1678+(n-50)*1734
elif(n<=200):
    sotien=50*1678+50*1734+(n-100)*2014
elif(n<=300):
    sotien=50*1678+50*1734+100*2014+(n-200)*2536
elif(n<=400):
    sotien=50*1678+50*1734+100*2014+100*2536+(n-300)*2834
else:
    sotien=50*1678+50*1734+100*2014+100*2536+100*2834+(n-400)*2927
print("Tổng số tiền:", sotien)