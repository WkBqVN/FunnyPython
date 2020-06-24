""" BÀI TẬP VỀ NHÀ BUỔI 05 - Tuple:
Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    Sau đó, unpack các phần tử trong một tuple.
Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
Bài 02: Viết chương trình đảo ngược một tuple.
Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
Bài 04: Cho 1 list chứa các tuple không rỗng.
    Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
"""

"""Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    Sau đó, unpack các phần tử trong một tuple."""
import random
bai00_tuple = random.sample(range(100),2),random.randint(1,20),random.choice(["abc","Hello","World"]),

for i in range(0,len(bai00_tuple)):
    a = bai00_tuple[i]
    print(f"unpack bai00_tuple = {a}")

"""Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple"""
bai01_tuple = (1,2,"Hello",4,5,)
trans_tuple_to_list = list(bai01_tuple)
print(type(trans_tuple_to_list))
bai01_tuple = tuple(trans_tuple_to_list)
print(type(bai01_tuple))

"""Bài 02: Viết chương trình đảo ngược một tuple."""
bai02_tuple = (1,2,3,4,5,)
reverse_tuple = bai02_tuple[::-1]
print("Tuple sau khi da duoc dao nguoc la: ",reverse_tuple)

"""Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple."""
bai03_list = [1,2,3,4,5,("Hello",1,2),5,6,7,9,("nothing")]
res = 0
check_flag = False
for i in bai03_list:
    if type(i) is tuple:
        check_flag = True
        res = bai03_list.index(i)
        break
    else:
        continue
print(("So luong phan tu den khi gap tuple la : ",res)if check_flag == True else "khong co phan tu dang tuple")

"""Bài 04: Cho 1 list chứa các tuple không rỗng.
  Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple."""
bai04_list = [(2, 5), (4, 1), (0, 0),(4,6),(1,2),(5,6,8),(8,8,7)]
for i in range(0,int(len(bai04_list)*(len(bai04_list)-1)/2)):
    for j in range(i+1,len(bai04_list)):
        if bai04_list[i][-1]>bai04_list[j][-1]:
            bai04_list[i],bai04_list[j] = bai04_list[j],bai04_list[i]
print("list tuple co cac phan tu cuoi tang dan la: ",bai04_list)

# SecondSolution(bai04)
# def takeLast(input_list):
#     return input_list[-1]
# bai04_list = [(2, 5), (4, 1), (0, 0),(4,6),(1,2),(5,6,8),(8,8,7)]
# bai04_list.sort(key = takeLast)
# print(bai04_list)

"""Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple."""
bai05_list_tuples = [(5,6),(1,2,3),(3,4,5),(5,6,4,2),(1,3,4,5,6,1)]
min_value_positon_2 = bai05_list_tuples[0][1]
index_of_res_tuple = 0
for i in bai05_list_tuples:
    if i[1] < min_value_positon_2:
        min_value_positon_2 = i[1]
        index_of_res_tuple = bai05_list_tuples.index(i)
print("tuple co phan tu thu 2 nho nhat la: ",bai05_list_tuples[index_of_res_tuple])


"""Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple."""
bai06_tuple = (1,2,3,4,5,6,7,8,9,10)
print("phan tu thu 4 la: {}".format(bai06_tuple[3]))
print("phan tu thu 4 tu cuoi len la: {}".format(bai06_tuple[-4]))

"""Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không."""
bai07_tuple_1 = (1,2,3,4)
bai07_tuple_2 = (2,7,8,9,10)
check_flags_bai07 = False
for i in bai07_tuple_1:
    if i in bai07_tuple_2:
        check_flags_bai07 = True
        break
    else:
        continue
print("2 tuple co phan tu chung" if check_flags_bai07 else "2 tuple khong co phan tu chung nao")

"""Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không."""
bai08_tuple = (1,1,1,1,1,1,1,1,1,1,)
check_flags = True
for i in range(1,len(bai08_tuple)):
    if bai08_tuple[i] != bai08_tuple[0]:
        check_flags = False
        break
print("cac phan tu cua tuple deu giong nhau" if check_flags else "cac phan tu cua tuple khong giong nhau")

"""Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực."""
bai09_tuple = (1,2,3,4,-1,-2,-3,6,-7,8,19)
res_max = bai09_tuple[0]
res_sum = 0
for i in bai09_tuple:
    res_sum += i
    if i > res_max:
        res_max = i
print("Gia tri lon nhat la: {} ; va tong cua cac gia tri trong tuple la: {}".format(res_max,res_sum))

"""Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
  Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên."""
bai10_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
res_list_bai10=[]
for i in bai10_list:
    if i.split('.')[-1] not in res_list_bai10:
        res_list_bai10.append(i.split(".")[-1])
print("Cac ten mien co trong list la : ",res_list_bai10)

"""Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím."""
import re
input_string = input("Moi ban nhap cau can tim tu dai nhat: ")
word_list = re.findall(r"[\w']+",input_string)
res = word_list[0]
for i in word_list:
    if len(i)> len(res):
        res = i
print("tu dai nhat trong cau ban go la : ",res)
