""" 
Project: Xếp loại học lực cả năm của học sinh.
Built by: Dravon.
Date: 18-10-2025.
"""
# Nhập điểm các môn học và tính điểm trung bình chung cả năm
a =float(input(" Nhập điểm toán: "))
b =float(input(" Nhập điểm văn: "))
c =float(input(" Nhập điểm anh: "))
d =float(input(" Nhập điểm lý: "))
e =float(input(" Nhập điểm hóa: "))
f =float(input(" Nhập điểm sinh: "))
g =float(input(" Nhập điểm sử: "))
h =float(input(" Nhập điểm địa: "))
i =float(input(" Nhập điểm GDCD: "))
# Xử lý dữ liệu
diemtrungbinh=((a+b+c)*2+(d+e+f+g+h+i))/12
# Điều kiện xếp loại học lực
# Điều kiện học lực giỏi
if diemtrungbinh >= 8.0:
    if all( x>= 6.5 for  x in [a,b,c,d,e,f,g,h,i]):
        print(" Xếp loại giỏi")
        # Điều kiện học lực khá
elif 6.5<= diemtrungbinh <=8.0:
    if all( x>=5.0  for x in [a,b,c,d,e,f,g,h,i]):
        print(" Xếp loại khá")
        # Điều kiện học lực trung bình
elif 5.0<= diemtrungbinh <6.5:
    if all( x>=3.5 for x in [a,b,c,d,e,f,g,h,i]):
        print(" Xếp loại trung bình")
        # Điều học lực yếu
else:
    print("Xếp loại yếu")
print(" Điểm trung bình cả năm là:", diemtrungbinh)
                                                # Built by Dravon