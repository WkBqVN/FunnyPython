""" BÀI TẬP VỀ NHÀ BUỔI 04 - List:
Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
"""

#bai00
import random;
print("Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.")
number_list_bai00 = [11,12,13,14,15,16,17,18,19,10]
print("list_bai00: ",end ="")
print(number_list_bai00)
new_list_bai00 = []
for i in range(0,5):
    new_list_bai00.append(random.choice(number_list_bai00))
print(new_list_bai00)

#bai01
print("Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.")
number_list_bai01 = [11,12,13,14,15,16,17,18,19,10]
print("list_bai01: ",end = "")
print(number_list_bai01)
tong = 0
tich = 1
for i in number_list_bai01:
    tong += i
    tich *= i
print("tong la {} va tich la {}".format(tong,tich))

#bai02
print("Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.")
number_list_bai02 = [11,12,13,14,15,16,17,18,19,10]
print("list_bai02: ",end = "")
print(number_list_bai02)
min = number_list_bai02[1]
max = number_list_bai02[1]
for i in number_list_bai02:
    if i > max:
        max = i
    elif i < min:
        min = i
    else:
        continue
print("Gia tri Max la: {} ; Gia tri Min la: {}".format(max,min))

#bai03
print("Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.")
s = 'x'
number_list_bai03 = [10,11,12,13,14,15,16,17,18,19]
print("list_bai03: ",end = "")
print(number_list_bai03,end = "; ")
print("String_bai_03: ",end = "")
print(s)
new_number_list_bai03 = []
for i in number_list_bai03:
    new_number_list_bai03.append(str(i)+s)
print(new_number_list_bai03)

#bai04
print("Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.")
number_list_bai04 = [10,11,12,13,14,15,16,17,18,19]
print("list_bai04: ",end = "")
print(number_list_bai04)
input_position = int(input("Moi ban nhap vi tri can tach: "))
if input_position > len(number_list_bai04):
    print("Output: {}".format(number_list_bai04))
else:
    first_part_number_list_bai04 = number_list_bai04[0:input_position]
    second_part_number_list_bai04 = number_list_bai04[input_position:len(number_list_bai04)]
print("Output : ")
print("First list spilit at posion {} : {}".format(input_position,first_part_number_list_bai04))
print("Second list spilit at positon {} : {}".format(input_position,second_part_number_list_bai04))

#bai05
print("Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list")
print("\t Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng")
number_list_bai05 = [10,10,12,13,14,19,19,17,18,19]
print("list_bai05: ",end = "")
print(number_list_bai05)
max_count = 0
most_number_appreance = 9999;
for i in number_list_bai05:
    if number_list_bai05.count(i) > max_count:
        max_count = number_list_bai05.count(i)
        most_number_appreance = i
print("Gia tri xuat hien nhieu nhat la : {} ; So lan xuat hien la : {} ".format(most_number_appreance,max_count))

#bai06
print("Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:")
print(" \t + Độ dài từ 2 trở lên")      
print(" \t \t + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau")
string_list_bai06 = ["hello","world","abcda","j","o-o"]
print("list_bai06: ",end="")
print(string_list_bai06)
res_list_bai06 =[]
res_count = 0
for i in string_list_bai06:
    if len(i) > 1:
        if i[0] == i[len(i)-1]:
            res_list_bai06.append(i)
            res_count += 1
print("So chuoi trong list thoa man de bai la : {}; Cac chuoi do la: {}".format(res_count,res_list_bai06))

#bai07
print("Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.")
first_list_bai07 = [1,2,3,4,5]
second_list_bai07 = [2,5,6,7,8]
print("Fist_list_bai07: ",end = "")
print(first_list_bai07)
print("Second_list_bai07: ", end = "")
print(second_list_bai07)
check_flags = False
for i in first_list_bai07:
    if i in second_list_bai07:
        check_flags = True
        break
    else:
        continue
print("2 mang co phan tu chung " if check_flags == True else "Khong co phan tu chung giua 2 mang")

# bai08
print("Bài 08: Cho list các số nguyên dương A.")
print("\t Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j")
number_list_bai08 = [1,4,6,2,5,7,8,3,11,3,15,9]
print("list_bai08: ",end="")
print(number_list_bai08)
res_list_bai08 =[]
count_list = 0
for i in range(0,len(number_list_bai08)):
    for t in range(i+1,len(number_list_bai08)):
        if number_list_bai08[i] > number_list_bai08[t]:
            count_list +=1
            res_list_bai08.append([number_list_bai08[i],number_list_bai08[t]])
print("+ So luong tap thoa man yeu cau de bai: {} \n+ Chi tiet cac tap {}".format(count_list,res_list_bai08))

# bai09
import numpy as np
print("Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).")
first_matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
second_matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
res_matrix = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
]
for i in range(0,3):
        for j in range(0,3):
                for k in range(0,3):
                        res_matrix[i][j] += first_matrix[i][k]*second_matrix[k][j]
print("Ma tran ket qua la: \n {}".format(np.array(res_matrix)))

#bai10
print("""
Bài 10:Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
""")
song_list_id = [1,2,1,3,2,7,4,2,5,5]
print("Song_list_id_bai10: {}".format(song_list_id))
res_list =[]
for i in song_list_id:
        if (i in res_list) == False:
                res_list.append(i)
print("Id cac bai hat ban da nghe la: {}".format(res_list))