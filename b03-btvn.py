""" BÀI TẬP VỀ NHÀ BUỔI 03 - String
Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
"""

#bai01
print("BTVN1 : ")
str = input("Moi ban nhap chuoi: ")
res_str = str.replace(str[0],'$')
print(res_str)

#bai02
print("BTVV2: ")
str_2 = input("moi ban nhap chuoi")
m = int(input("moi ban nhap so can nhap: "))
res2 = str_2[0:m]+ str_2[m+1:]
print(res2)

#bai03
print("BTVN3: ")
str_3 = input("moi ban nhap chuoi de xoa so le: ")
print(str_3[1::2])

#bai04
print("BTVN4: ")
str_4 = input("moi ban nhap chuoi :")
if len(str_4) < 2:
    print(" ")
else:
    print(str_4[0:2] + str_4[-2:len(str_4)])

#bai05
print("BTVN5: ")
str_5 = input("moi ban nhap chuoi: ")
max_value = str_5[0]
min_value = str_5[0]
for i in str_5:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i
    else:
        continue
print(max_value +" "+min_value)

#bai06
print("BTVN6: ")
str_6 = input("Moi ban nhap 1 chuoi: ")
res =  ""
for i in str_6:
    if 65 <= ord(i) <= 90:
        res += chr(ord(i)+32)
    elif 97 <= ord(i) <= 122:
        res += chr(ord(i)-32)
    else:
        res += i
print(res)
