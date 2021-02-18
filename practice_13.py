
def abc191_remove_it():
    n, x = map(int, input().split())
    str_a = str(input())

    list_a = [int(a) for a in str_a.split()]

    list_result = []

    for int_a in list_a:
        if not x == int_a:
            list_result.append(str(int_a))
    
    p = ' '.join(list_result)

    print(p)

if __name__ == "__main__":
    abc191_remove_it()
    