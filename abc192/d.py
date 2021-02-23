def d():
    x = str(input())
    m = int(input())

    list_x_num = [int(s) for s in x]
    max_x = max(list_x_num)

    left = max_x + 1
    right = 10 ** 18

    # xが1桁の場合
    if int(x) < 10:
        if int(x) > m:
            print(0)
            return
        else:
            print(1)
            return
    
    while left <= right:
        mid_f = m_n_num(list_x_num, int((left + right) / 2))
        if mid_f > m:
            right = int((left + right) / 2) - 1
        else:
            left = int((left + right) / 2) + 1
    
    print(right - max_x)
        

def m_n_num(list_x_num, n):
    # xをn進数に変換する
    # xはlistに変換して引き渡す
    i = len(list_x_num) - 1
    calc_x = 0
    while i >= 0:
        calc_x += (n ** i) * list_x_num[len(list_x_num) - 1 - i]
        i -= 1
    return calc_x

    
    

if __name__ == "__main__":
    d()