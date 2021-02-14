
def abc087b_coins():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    a_num, b_num, c_num = 0, 0, 0
    count = 0

    while a_num <= a:
        b_num = 0
        while b_num <= b:
            c_num = 0
            while c_num <= c:
                if 500 * a_num + 100 * b_num + 50 * c_num == x :
                    count += 1
                
                c_num += 1
            b_num += 1
        a_num += 1
    
    print(count)


if __name__ == "__main__":
    abc087b_coins()
