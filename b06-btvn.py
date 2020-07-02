""" BÀI TẬP VỀ NHÀ BUỔI 06 - DICTIONARY:
Bài 00: Viết chương trình tính tích các phần tử trong một dict
Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}
Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}
"""

# Bài 00: Viết chương trình tính tích các phần tử trong một dict
# khong the thuc hien neu dict co' 2 key deu co value la string vi string khong the nhan voi string
print("#bai00")
my_dict_00 = {"mot" : 1, "hai" : 2, "ba": 3}
multi_dict_value = 1
for i in my_dict_00:
    multi_dict_value *= my_dict_00.get(i)
print(multi_dict_value)

# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
print("#bai01")
my_dict_01 = {
     1:1,
     2:1,
     5:2,
     6:3,
     "mot": 8,
     8: 9
}
min_value = 9999;
max_value = 0;
for i in my_dict_01:
    if min_value > my_dict_01.get(i):
        min_value = my_dict_01.get(i)
    if max_value < my_dict_01.get(i):
        max_value = my_dict_01.get(i)
print("Min is {} and Max is {}".format(min_value,max_value))

#Solution2 - bai01
# max_value = max(my_dict_01.values());
# min_value = min(my_dict_01.values());
# print(min_value)
# print(max_value)

# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
print("#bai02")
my_dict_02 = {
    1:1,
    2:2,
    6:3,
    3:"mot",
    4: 5
}
print(sorted(my_dict_02))

# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
print("#bai03")
my_dict_03 = {
    1:1,
    2:2,
    "word": "hello",
    "sentence": "Xin chao",
    "chao hoi": "Xin chao",
    5: "Xin chao",
    6: 6
}
data_set = set();
for i in my_dict_03:
    data_set.add(my_dict_03.get(i))
print(data_set)

#Solution2-bai03
# test_set = set(my_dict_03.values())
# print(test_set)

# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
print("#bai04")
my_dict_04 = {
    1:1,
    5:2,
    6:3,
    8:4,
    12:6,
    15:1,
    16:2,
    200:"xin chao",
}
res_list_key_max = set();
while len(res_list_key_max) < 3:
    res_list_key_max.add(max(my_dict_04.keys()))
    my_dict_04.pop(max(my_dict_04.keys()))
print(res_list_key_max)


# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
import random
print("#bai05")
dict_range = random.randint(5,10)
my_dict_bai_05 = {}
for i in range(0,dict_range):
    list_range = random.randint(5,15)
    input_list = []
    for j in range(0,list_range):
        input_list.append(random.randint(1,20))
    my_dict_bai_05[i] = input_list
print(my_dict_bai_05)
take_5_element_dict = lambda x : (my_dict_bai_05.get(x)[4])
for i in range(0,dict_range):
    print(take_5_element_dict(i))

# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
print("#bai06")
my_dict_06_01 = {
    "hello":"Xin chao",
    1 : 2,
    2 : 3,
    3 : "Goodbye",
    "number" : 2
}
my_dict_06_02 = {
    "hello" : "what",
    2: "why",
    "chuoi" : 3
}
res_set = set();
for i in my_dict_06_01:
    if i in my_dict_06_02:
        res_set.add(i)
print(res_set)

#Solution2_bai06
# test_res_set_06 = my_dict_06_01.keys()& my_dict_06_02.keys()
# print(test_res_set_06)

# Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}
print("#bai07")
my_dict_07 = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
list_key = ["name","salary","Other"]
res_dict = {};
for i in list_key:
    if i in my_dict_07:
        res_dict[i] = my_dict_07.get(i);
print(res_dict)

# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
print("#bai08")
my_dict_08 ={
    "hello":1,
    2: 3,
    10 :6,
    19: 200,
    18:178,
    "Goodbye" : 100,
    "end": 10
}
res_set = set();
while len(res_set) < 3:
    key_max = max(my_dict_08,key=my_dict_08.get)
    res_set.add(key_max)
    my_dict_08.pop(key_max)
print(res_set)

    

# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
print("#bai09")
input_string_09 = "Toi la Khoa, toi den tu Viet Nam, ban den tu dau, noi do the nao?"
res_dict = {};
for i in input_string_09:
    res_dict[i] = input_string_09.count(i)
print(res_dict)

# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
print("#bai10")
def demSoTu(input):
    return input.count(chr(32))+ input.count("\n") -1

doan_van_ban = """
Trich bai hat:
Ngan nam con song so bo cat
Anh viet khuc ca ve gio
Gui con thuyen tinh yeu
Goodbye my Friend
"""

print(demSoTu(doan_van_ban))

# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
print("#bai11")
input_list = [
    {'item': 'item1', 'amount': 400}, 
    {'item': 'item2', 'amount': 300}, 
    {'item': 'item1', 'amount': 750}
]
res_dict = {}
for i in input_list:
    input_list_element = list(i.values())
    if input_list_element[0] in res_dict.keys():
        res_dict[input_list_element[0]] += input_list_element[1]
    else:
        res_dict[input_list_element[0]] = input_list_element[1]
print(res_dict)


