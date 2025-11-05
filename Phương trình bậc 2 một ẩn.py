#Project: Phuong trinh bac 2 mot an.
#Built by: Dravon.
#Date:17-10-2025.
#Khai bao thu vien
from math import sqrt # sqrt : can
print(" Phương trình bậc hai")
# Nhap so lieu tu ban phim
a=float(input(" Nhập hệ số a :"))
b=float(input(" Nhập hệ số b :"))
c=float(input(" Nhập hệ số c :"))
# Xu ly so lieu
# Xet nghiem lan 1
# Dieu kien 1
# xet a bang 0
if a==0:
    #Dieu kien 2
        if b==0:
            # Dieu kien 3
            if c==0:
                print("Phuong trinh vo so nghiem")
            else:# xet c khac 0
                print("Phuong trinh vo nghiem")
        else:# xet b khac 0
            # Dieu kien 4
            if c==0:
                print(" Nghiem cua phuong trinh la x = 0")
            else:# xet c khac 0
                x=float(-c/b)# xet nghiem phuong trinh bac nhat mot an
                print(" Nghiem cua phuong trinh la x = ", x)
 # Xet nghiem lan 2                     
else:# xet a khac 0
    m = (b**2) - (4*a*c)
    # Dieu kien 5
    if m < 0:# xet m be hon 0
        print(" Phuong trinh vo nghiem")
        # Dieu kien 6
    elif m==0:# xet m bang 0
        x=-b/(2*a)# xet nghiem kep
        print(" Nghiem cua phuong trinh la x =",x)
    else:# xet m lon hon 0
        print("Phuong trinh gom 2 nghiem phan biet x1,x2")
        x1= (-b-sqrt(m))/(2*a)# xet nghiem phan biet
        x2= (-b+sqrt(m))/(2*a)# xet nghiem phan biet
        print(" Nghiem thu 1:%.4f" %x1)# lay 4 so sau dau phay
        print(" Nghiem thu 2:%.6f" %x2)# lay 6 so sau dau phay
                                                                    #Built by Dravon


