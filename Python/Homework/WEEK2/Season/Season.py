'''Season'''
mon = int(input())
day = int(input())
winter = [1,2,3]
spring = [4,5,6]
summer = [7,8,9]
fall = [10,11,12]
e = [3,6,9]
if mon == 12 and day >= 21:
    mon = 1
if day >= 21:
    if mon in e:
        mon += 1
if mon in winter:
    print("winter")
if mon in spring:
    print("spring")
if mon in summer:
    print("summer")
if mon in fall:
    print("fall")
