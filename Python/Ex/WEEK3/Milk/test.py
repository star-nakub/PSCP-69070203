"""milk"""
a = int(input()) # prices
b = int(input()) # every x cap
c = int(input()) # get x bottle
d = int(input()) # money

bot = d // a
cap = bot // b
final = (cap*c) + bot

print(final)
