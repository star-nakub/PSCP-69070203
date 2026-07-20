'''AR TikTok'''
def main():
    '''main'''
    ar = input().split(" ")
    r = int(ar[0])
    x = int(ar[1])
    y = int(ar[2])
    if r**2 == (x**2 + y**2):
        print("ON")
    elif r**2 > x**2 + y**2:
        print("IN")
    else:
        print("OUT")
main()
