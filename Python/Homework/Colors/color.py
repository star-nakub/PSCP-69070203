"""name"""
def main():
    '''name'''
    #code
    c1 = str(input())
    c2 = str(input())
    color = ["Red","Yellow","Blue"]
    if c1 in color and c2 in color:
        if c1 == "Red" and c2 == "Yellow" or c1 == "Yellow" and c2 =="Red":
            print("Orange")
        elif c1 == "Red" and c2 == "Blue" or c1 == "Blue" and c2 == "Red":
            print("Violet")
        elif c1 == "Yellow" and c2 == "Blue" or c1 == "Blue" and c2 == "Yellow":
            print("Green")
        elif c1 == c2 and c2 == c1:
            print(c1)
        else:
            print("Error")
    else :
        print("Error")
main()
