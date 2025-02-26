# channel_name = "an cai con bo"

# print(channel_name.replace("bo", "heo"))
# from math import*



# number = 36

# print(ceil(number))

# print(sqrt(number))

#-----------------------------------------------------------------

# name = input("nhap ten cua ban: ")
# age = input("nhap tuoi cua ban: ")


# print(f"xin chao {name} nam nay ban {age}")

#-----------------------------------------------------------------

# num1 = input("Nhap so thu 1: ")
# num2 = input("Nhap so thu 2: ")

# sum = int(num1) + float(num2)

# print("Ket qua:", sum)

#-----------------------------------------------------------------

# number = 1
# my_age = 20
# my_wife_age = 19

# text = "so nguoi yeu cua toi: {}"
# vị trí đặt số vào

# text = "Nam nay vo toi {1} tuoi con toi {0} tuoi"

# print(text.format(my_age, my_wife_age))



# print(text.format(number))

#-------------------------------------------------------------
# dữ liệu dạng danh sách

# teams = ["VN", "Thai", "Lao", "Cam", "Indo"] 
# # dấu ngoặc vuông python sẽ hiểu là danh sách
# teams[1] = "Sin"

# print(teams[-1])
# print(teams[1:])
# # 1: in đội bóng từ vọ trí 1 và các dội ở phía sau nó

# print(teams[1:4])


# ---------------------------------------------------------------
# các hàm thao tác với list

# student_names = ["Bao", "Bao", "Phu", "Ngan", "Thu", "Ha"]
# math_scores = [10, 2, 4, 5, 8, 7]

# student_names.extend(math_scores)
# student_names.append("Nhung")
# student_names.insert(1, "Huyen")
# student_names.remove("Phu")
# student_names.pop() loai bo phan tu cuoi
# print(student_names.index("Bao"))
# print(student_names.count("Bao"))
# student_names.sort()
# math_scores.sort()
# math_scores.reverse()

# student_names_2 = student_names.copy()

# print(student_names)
# -------------------------------------------------------------------

# cấu trúc dữ liệu tuple 

# coordinates = (123, 456)

# coordinates_2 = [(1, 2), (3,4), (5,6)]
# # khác với list là này dùng () 
# # giá trị của tuple không thể chỉnh sửa
# # sử dụng khi dữ liệu không thay đổi

# print(coordinates_2[1])

# ---------------------------------------------------------------------

# Thao tác với hàm

# def say_hello(name, email):
#     print(f"Hello, my name is {name}")
#     print(f"Email la: {email}")

# print("Bắt đầu")
# say_hello("Bao", "thaibao1852004@gmail.com")
# print("ket thuc")
# -------------------------------------------------------------------

# lệnh return trong hàm

# def add(a, b):
#     return a + b

# res = add(2, 3)
# print(res)

# ------------------------------------------------------------------
# lệnh if, elif, else

# a = 110
# b = 100

# def compare():
#     if a < b:
#         print("a nho hon b")
#     elif a == b:
#         print("a bang b")
#     else:
#         print("a lon hon b")

# compare()

# ------------------------------------------------------------------

# các toán tử logic

a = 200
b = 50
c = 20

# if (a > b) and (a > c):
#     print("a la so lon nhat")

# if (a == b) or (a == c):
#     print("co it nhat mot so bang gia tri a")
# else:
#     print("adu")

# a = 100
# b = 200

# if not a > b:
#     print("a khong lon hon b")
# -------------------------------------------------------------------

# cải tiến ứng dụng máy tính

# def calculator():
#     num1 = float(input("Nhap vao so thu 1: "))
#     operator = input("Nhap toan tu: ")
#     num2 = float(input("Nhap vao so thu 2: "))

#     if(operator == "+"):
#         print(num1 + num2)
#     elif(operator == "-"):
#         print(num1 - num2)
#     elif(operator == "*"):
#         print(num1 * num2)
#     elif(operator == "/"):
#         print(num1 / num2)
#     else:
#         print("Toan tu khong hop le!!!")

# calculator()

# ---------------------------------------------------------------------
# cấu trúc dữ liệu dictionary

# english_vietnamese_dictionary = {
#     "Hello": "Xin chao",
#     "Goodbye": "Tam biet",
#     "Morning": "buoi sang",
#     "bread": "banh mi",
#     "Coffee": "ca phe",
#     "tea": "Tra",
#     "Milk": "Sua",
#     "Beer": "bia"

#     # tất cả các từ khóa phải là duy nhất không đc trung lắp
# }

# # print(english_vietnamese_dictionary["Hello"])
# print(english_vietnamese_dictionary.get("dog", "Tu khoa nay khong ton tai!!!"))

# ---------------------------------------------------------------------------
# vòng lập while

# i = 1
# while i < 10:
#     print("du ma")
#     i+=1
# print("adu vay!!!")

# -------------------------------------------------------------------------------

# build trò chơi đoán từ

# secret_word = "Python"
# hint = "Day la 1 ngon ngu lap trinh"
# guess = ""
# guess_cnt = 0

# print(hint)
# while guess != secret_word:
#     if guess_cnt < 3:
#         guess = input("Day la tu gi: ")
#         guess_cnt+=1
#     else:
#         break

# if guess == secret_word:
#     print("Ban da doan chinh xac!")
# else:
#     print("Ban da that bai!!!")

# ------------------------------------------------------------------------------

# vòng lập for

# name = "Thai Bao"

# teams = ["VN", "LAO", "THAILAN"]

# for i in range(1, 11):
#     if i == 1:
#         print("Day la phan tu dau tien trong mang")
#     else:
#         print(f"Day la phan tu o vi tri {i} trong mang")

# --------------------------------------------------------------------------------

# build hàm tính lũy thừa

# def calculate_power(base_num, exponent):
#     result = 1
#     for i in range(exponent):
#         result = result * base_num
#     return result

# ans = calculate_power(2, 3)
# print(ans)

# ----------------------------------------------------------------------------------

# Mảng 2 chiều, các vòng lặp lồng nhau

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in matrix:
#     for j in i:
#         print(j)

# ------------------------------------------------------------------------------------

# Ứng dụng chuyển đổi ngôn ngữ 

# def translate(text):
#     translation = ""
#     for i in text:
#         if i.lower() in "áàảãạăắẳẵặâấầẩẫậ":
#             if i.isupper():
#                 translation = translation + "A"
#             else:
#                 translation = translation + "a"
#         else:
#             translation = translation + i
#     return translation

# text = input("Nhap vao van ban ma ban muon dich: ")

# ans = translate(text)
# print(ans)

# ------------------------------------------------------------------------------------------
# xử lý ngoại lệ

# try:
#     print(text)
# except:
#     print("Co loi xay ra vui long lien he tt tu van dde dduocj ho tro")

# try:
#     num1 = int(input("Nhập tử số: "))
#     num2 = int(input("Nhập mẫu số: "))
#     ans = num1 / num2  
#     print(f"Thương của phép chia là: {ans}")
# except ZeroDivisionError:
#     print("Mẫu số phải khác 0!!!")
# except ValueError:
#     print("Dữ liệu phải là các số nguyên!!!")
# except:
#     print("Có lỗi xảy ra vui lòng liên hệ trung tâm tư vấn!!!")

# --------------------------------------------------------------------------------------------

# Đọc file

# phone_book = open("phone_book.txt", "r")

# # print(phone_book.readlines())
# for i in phone_book.readlines():
#     i = i.replace("\n", "")
#     # xóa \n
#     print(i)


# phone_book.close()
# sau khi đọc file phải đóng file lại

# -----------------------------------------------------------------------------------------
# Ghi dữ liệu vào file

# phone_book = open("phone_book.txt", "a")
# phone_book.write("Adu-132423452")
# không có \n thì nó sẽ ghi dính liền với dòng cuối
# phone_book.write("\nAdu-132423452")
# phone_book.write("\nAduVIp-037823452")

# phone_book = open("index.html", "w")
# # w sẽ ghi đè lên dữ liệu cũ còn a thêm dữ liệu mới ở cuối file
# # w cũng có thể tạo ra một file mới
# phone_book.write("<p>Hello</p>")
# # phone_book.write("\nAduVIp-037823452")

# phone_book.close()
# -------------------------------------------------------------------------------------------

# Sử dụng module, thư viện bên thứ 3

# from random import*

# pi = 3.14
# big_six_teams = ["VN", "LAO", "CAM", "THAI", "SIN", "INDO"]

# def roll_dice(number):
#     # hàm này hoạt động như việc tung xúc sắc 
#     return randint(1, number)
# random từ 1 đến số mình truyền vào  

# ------------------------------------------------------------------------------------
# class và object

# class Car:
#     def __init__(self, name, brand, color):
#         self.name = name
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"Bạn đang lái chiếc xe {self.name} hãng xe {self.brand} màu {self.color}")

# KiaMorning = Car("Kia morning", "Kia", "Blue")
# KiaMorning.drive()

# build ứng dụng thi trắc nghiệm

from Demo import Quiz

questions = [
    "Câu 1. Đội bóng nào về nhì WC 1994?\nA. Brazil\nB. Italia\nC. Đức\n",
    "Câu 2. Đội bóng nào vô định WC 1998?\nA. Argentina\nB. Pháp\nC. Brazil\n",
    "Câu 3. Nước nào là chủ nhà WC năm 2002?\nA. Qatar\nB. Đức\nC. Hàn Quốc + Nhật Bản\n",
]

quizzes = [
    Quiz(questions[0], "B"),
    Quiz(questions[1], "B"),
    Quiz(questions[2], "C")
]

def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.question)
        user_input = input("Nhập câu trả lời: ")
        if user_input.lower() == quiz.answer.lower():
            score+=1
    print(f"\n--> Kết quả: bạn đã trả lời đúng {score}/{len(quizzes)} câu!!!")

run_quizzes(quizzes)