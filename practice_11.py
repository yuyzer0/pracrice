
def abc086c_traveling():

    n = int(input())

    i = 0
    place_list = []
    place_info_list = []

    while i < n:
        place_list.append(str(input()))
        i += 1
    
    before_place_info_list = []
    for place_info in place_list:
        tmp = place_info.split()
        place_info_list = [int(s) for s in tmp]

        if len(before_place_info_list) == 0:
            move = place_info_list[1] + place_info_list[2]
            time = place_info_list[0]
        else:
            move = place_info_list[1] + place_info_list[2] - before_place_info_list[1] - before_place_info_list[2]
            time = place_info_list[0] - before_place_info_list[0]
        
        if not((time - abs(move)) % 2 == 0) or abs(move) > time:
                print("No")
                return

        before_place_info_list = place_info_list

    print("Yes")

if __name__ == "__main__" :
    abc086c_traveling()