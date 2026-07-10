"""name"""
def main():
    '''name'''
    #code
    name = str(input())
    sname = str(input())
    age = str(input())
    if len(name) >= 5 and len(sname) >= 5 :
        print(f"{name[0]+name[1]+sname[-1]+age[-1]}")
    else:
        print(f"{name[0]+age+sname[-1]}")
main()
