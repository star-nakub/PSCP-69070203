"""คำนวณราคาสินค้าโปรโมชั่น"""
a,b,c = map(int, input().split())
price = a*25+b*40+c*55
total = a+b+c
if total >= 3:
    print(int(price * 0.9))
else:
    print(price)
