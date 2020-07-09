""" BÀI TẬP VỀ NHÀ BUỔI 07 - Function:
Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào
Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
Bài 06: Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
        Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy
Bài 12: Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
"""

# Bài 01: Viết hàm
#         def max_min(*numbers) 
#     trả lại cả giá trị max, min của nhiều số được truyền vào
def max_min(input_list):
    max_value =0
    min_value = 9999
    for i in input_list:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
        else:
            continue
    print("Max of input Number is: {}, Min of input Number is: {}".format(max_value,min_value))
input_list = []
print("Moi ban nhap day so can tim max_mix. ket thuc = end")
while True:
    x = input()
    if x == 'end':
        break
    input_list.append(int(x))
max_min(input_list)

# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str
def reverse_string(str):
    return str[::-1]
input_str = "vo van khoa"
print(reverse_string(input_str))

# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
def is_perfect(n):
    res_sum = 0;
    for i in range(1,n):
        if(n%i ==0):
            res_sum += i
    return True if res_sum == n else False
input_number = int(input("moi ban nhap so:"))
print(is_perfect(input_number))


# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
def is_prime(n):
    check_flags = True
    if n == 2 :
        pass
    elif n < 2 :
        check_flags = False
    else:
        for i in range (2,int(n/2)+1):
            if(n%i == 0):
                check_flags =  False
                break

    return check_flags
    
input_number_n = int(input("Moi ban nhap so can kiemtra so nguyen to: "))
print(is_prime(input_number_n))


# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
def count_upper_lower(input_str):
    count_upper =0
    count_lower =0
    for i in input_str:
        if ( 95 <= ord(i) <= 122):
            count_lower +=1
        elif( 65 <= ord(i) <= 97):
            count_upper += 1
        else:
            continue
    print("Upper is: {} ; Lower is {}".format(count_upper,count_lower))

input_str = input("moi ban nhap chuoi: ")
count_upper_lower(input_str)

# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần

def is_pangram(input_str):
    check_flag = True
    for i in range(97,123):
        if (chr(i) not in input_str.lower()):
            check_flag = False
            break
    return check_flag
pangram_str = "The quick brown fox jumps over the lazy dog"
other_str = "Hello How are you"
print(is_pangram(pangram_str))
print(is_pangram(other_str))



# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
def create_maxtrix(n,m):
    matrix = [[0 for x in range(n)] for y in range(m)]
    for i in range(n):
        for j in range(m):
            matrix[j][i] = i*j
    return matrix
so_hang_ma_tran = int(input("Moi ban nhap so hang: "))
so_cot_ma_tran = int(input("Moi ban nhap so cot ma tran: "))
print(create_maxtrix(so_cot_ma_tran,so_hang_ma_tran))


# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
def body_mass_index(m, h):
    return m/(h**2)
def bmi_information(m, h):
    output_info = ""
    if(body_mass_index(m,h) < 18.5):
        output_info ="gay"
    elif 18.5 <= body_mass_index(m,h) <= 24.9:
        output_info =" Binh Thuong"
    elif 25 <= body_mass_index(m,h) <= 29.9:
        output_info ="Thua can"
    elif 30 <= body_mass_index(m,h) <= 34.9:
        output_info ="Beo Phi Cap 1"
    elif 35 <= body_mass_index(m,h) <= 39.9:
        output_info ="Beo Phi Cap 2"
    else:
       output_info ="Beo Phi Cap 3"
    print("BMI cua ban la : {}, the trang cua ban la: {}".format(body_mass_index(m,h),output_info))

chieu_cao = float(input("Moi ban nhap chieu cao(Tinh theo don vi meter): "))
can_nang = int(input("Moi ban nhap can nang(tinh theo don vi kg): "))
bmi_information(can_nang,chieu_cao)
            

# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
def change_upper_lower(str):
    res_string = ""
    for i in str:
        if(ord(i) in range(65,91)):
            res_string += chr(ord(i)+32)
        elif (ord(i) in range(97,123)):
            res_string += chr(ord(i)-32)
        else:
            continue
    return res_string
input_string = input("Moi ban nhap chuoi: ")
print(change_upper_lower(input_string))

# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
def tinh_so_le(odd_number,n):
    if((n%10)%2 ==1):
        odd_number +=1
    if(int(n/10)==0):
        return odd_number
    else:
        return tinh_so_le(odd_number,int(n/10))

input_number = int(input("Moi ban nhap so : "))
print(tinh_so_le(0,input_number))


# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy

def de_quy_tribonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif (n==2):
        return 1
    else:
        return de_quy_tribonacci(n-1) + de_quy_tribonacci(n-2) + de_quy_tribonacci(n-3)
def khong_de_quy_tribonacci(n):
    res_tribonacci = 0;
    Number_0 = 0
    Number_1 = 1
    Number_2 = 1
    if ( n == 0 ):
        return 0;
    elif (n==1):
        return 1;
    elif (n == 2):
        return 1;
    for i in range(3,n+1):
        res_tribonacci = Number_2 + Number_1 + Number_0
        Number_0 = Number_1
        Number_1 = Number_2
        Number_2 = res_tribonacci
    return res_tribonacci
n = int(input("Moi ban nhap so tribonacci can tinh: "))
#ket qua tu ham de quy
print(de_quy_tribonacci(n))
#ket qua ham khong de quy
print(khong_de_quy_tribonacci(n))



# Bài 12: Viết hàm
#         def find_x(a_list, x)
# #     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
def find_x(a_list,x):
    res_list =[]
    for i in range(len(a_list)):
        if a_list[i] == x:
            res_list.append(i)
    if not res_list:
        return -1
    else:
        return res_list
x = input("Moi ban nhap yeu to can kiem tra: ")
check_list = ["abc","hello","iiii","khoa","hello","abc","abc"]
print(find_x(check_list,x))
