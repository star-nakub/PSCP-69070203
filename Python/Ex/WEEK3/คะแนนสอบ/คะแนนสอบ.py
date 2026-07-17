'''numbernaja'''
def numja():
    '''numberja'''
    times = int(input())
    list_num = []
    for _ in range (1,times+1) :
        val = int(input())
        list_num.append(val)
        mac = max(list_num)
    print(max(list_num))
    print(list_num.count(mac))
numja()
