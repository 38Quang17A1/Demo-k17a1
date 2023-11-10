
#Tính cước xe taxi:
loaixe=int(input("Loại xe:"));
sokm=int(input("Số km:"));
tgiancho=int(input("Thời gian chờ:"));

if(tgiancho<5):
     tiencho=0 
elif(tgiancho>=6):
     tiencho=tgiancho*800
print("Tiền chờ:",tiencho)
sotien=0
if(loaixe==4):
   if(sokm<=20):
        sotien=12100*sokm
   elif(sokm>=21):
        sotien=10000*sokm 

if(loaixe==7):
   if(sokm<30):
        sotien=14100*sokm  
   elif(sokm>=31):
        sotien=12000*sokm
print("Tiền di chuyển:", sotien)
tiencuoc= tiencho + sotien
print("Tiền cước:", tiencuoc)  