
def abc083b_some_sums():
    n, a, b = map(int, input().split())
    tmp = 1
    tmp_list = []
    
    while tmp <= n:
        digit_list = [int(s) for s in str(tmp)]
        sum_digit = sum(digit_list)
        if sum_digit >= a and sum_digit <= b :
            tmp_list.append(tmp)
        tmp += 1
    
    print(sum(tmp_list))

if __name__ == "__main__":
    abc083b_some_sums()

