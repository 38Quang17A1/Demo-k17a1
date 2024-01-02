#ktra số nguyên tố
def so_ngto(n):
    if n<0:
        return "Đây ko phải số ngto."
    else:
        for i in range(2,n):
            if n%i==0:
                return "Đậy là số ngto."
            else:
                return "Đây ko phải số ngto."
n=eval(input("Nhập n:"))
print(so_ngto(n))

#ktr số chính phương
import math
def so_cp(n):
    if n<0:
        return "Nhập số nguyên dương."
    else:
        for i in range(2,n+1):
            if math.sqrt(n)**2==n:
                return "Đây là số chính phương."
            else:
                return "Đây ko phải số chính phương."
n=eval(input("Nhập n:"))
print(so_cp(n)) 

#ktra số hoàn hảo
def so_hh(n):
    tong=0
    if n<0:
        return "Nhập số nguyên dương."
    else:
        for i in range(1,n):
            if n%i==0:
               tong+=1
               return "Đây là số hoàn hảo."
            else:
                return "Đây ko phải số hoàn hảo"
n=eval(input("Nhập n:"))
print(so_hh(n))

#ktra số lẻ số chẵn
def ktr_so(n):
    if n%2==0:
        return "Đây là số chẵn."
    else:
        return "Đây là số lẻ."
n=eval(input("Nhập n:"))
print(ktr_so(n))

#ktr số fibonacci
def kiem_tra_so_fibonacci(so_can_kiem_tra):
    flag = False
    #so fibonacci la so sao cho 5*x^2 + 4 hoac 5*x^2 - 4
    #co gia tri la so chinh phuong
    k_1 = 5*(so_can_kiem_tra**2) + 4
    k_2 = 5*(so_can_kiem_tra**2) - 4
    for i in range(1,k_1):
        if i**2 == k_1:
            flag = True
            return flag
    for i in range(1,k_2):
        if i**2 == k_2:
            flag = True
            return flag
    return flag

#ktra số đối xứng(<1000)
def so_dx(n):
    if n%11==0 & n%111==0:
        return "Đây là số đxung."
    else:
        return "Đây kphai số đxung."
n=eval(input("Nhập n:"))
print(so_dx(n))