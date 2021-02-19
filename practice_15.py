def abc190_b():
    list_num = [int(s) for s in str(input()).split()]

    n = list_num[0]
    list_strxy = []

    i = 0
    while i < n:
        str_xy = str(input())
        list_strxy.append(str_xy)
        i += 1
    
    for xy in list_strxy:
        int_xy = [int(s) for s in str(xy).split()]
        if int_xy[0] < list_num[1] and int_xy[1] > list_num[2]:
            print("Yes")
            return
    
    print("No")

if __name__ == "__main__":
    abc190_b()