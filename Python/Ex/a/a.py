# """DocString"""
# def getName(name):  # name จะมีรูปแบบเป็น "Name : {ชื่อ}"
#     """DocString"""
#     print(name[7:])

# # เรียกฟังก์ชัน
# getName("Name : Ann")
# """DocString"""
# def getTitle(text): #text เป็น string"
#     """DocString"""
#     print(text[:1])
# getTitle("PSCP")

# """DocString"""
# def before_last(text): #text เป็น string"
#     """DocString"""
#     #จงเขียนโปรแกรมเพื่อแสดงค่าตัวอักษรตัวก่อนสุดท้ายของตัวแปร text ตัววิธี String slice
#     print(text[-2])
# #จงเรียกฟังก์ชั่น before_last เพื่อแสดงตัวอักษรตัวก่อนสุดท้ายของ "vanilla"
# before_last("vanilla")

# """DocString"""
# def show(text): #text เป็น string"
#     """DocString"""
#     #จงเขียนโปรแกรมเพื่อแสดงค่าตัวอักษรของข้อความtext บรรทัดละตัว ด้วยวิธี for loop in string
#     for i in text:
#         print(i)
# show("New")
# #จงเรียกฟังก์ชั่น show เพื่อแสดง "New"

# def banana_finder(text):
#     #ตรวจสอบตัวแปร text ว่ามีคำว่า "banana" ที่ index ไหน แต่ถ้าไม่เจอให้แสดงผล "banana is not found"
#     x = text.find("banana")
#     if x == -1:
#         print("banana is not found")
#     else:
#         print(x)
# banana_finder("I love banana")
# #เรียกใช้ฟังก์ชั่น banana โดยใส่ข้อความ "I love banana" เป็น argument

# def space_checker(text):
#     #นำตัวแปร text มาตรวจสอบว่ามี whitespace (" ") ในข้อความหรือไม่ หรือไม่
#     #หากมีให้แสดงข้อความ "This text has whitespace"
#     #หากไม่มีให้แสดง "This text doesn't have whitespace"

#     if " " in text:
#         print("This text has whitespace")
#     else:
#         print("This text doesn't have whitespace")

# #เรียกใช้ฟังก์ชั่น space_checker() โดยใส่ข้อความ "Hello World"
# space_checker("Hello World")

#สร้างฟังก์ชัน main เพื่อแสดงค่าของตัวแปร b ให้พี่หน่อย พร้อมแก้เรื่อง Line too long ของตัวแปร b
def main():
    b = "1234567890123456789012345678901234567890123456789\
    012345678901234567890123456789012345678901234567890"
    print(b)
main()