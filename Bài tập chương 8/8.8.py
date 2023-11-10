m=int(input("Loại phòng:"));
q=int(input("Số đêm:"));

if(m==1):
  st=1260000
elif(m==2):
  st=1550000
elif(m<5):
  st=1830000
elif(m<7):
  st=2120000
elif(m==7):
  st=2540000
elif(m==8):
  st=4800000
if (q==1):
  tt=st
elif(q<=3):
  tt=(st-st*0.25)*q
else:
  tt=(st-st*0.3)*q
print("Thanh toán:", tt)