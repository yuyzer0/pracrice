def abc088b_cardGameForTwo():
    n = int(input())
    str_a = str(input())

    list_a = [int(s) for s in str_a.split()]

    a_choice = []
    b_choice = []

    i = 0

    while i < n :
        a_choice.append(max(list_a))
        list_a.remove(max(list_a))
        i += 1

        # 奇数回のために回数判定
        if not i < n:
            break

        b_choice.append(max(list_a))
        list_a.remove(max(list_a))
        i += 1
    
    print(sum(a_choice) - sum(b_choice))

if __name__ == "__main__" :
    abc088b_cardGameForTwo()
