def solve():
    n ,x = map(int, input().split())
    list_a = [str(s) for s in str(input()).split()]

    result_list = []
    for a in list_a:
        if a == str(x):
            continue
        else: 
            result_list.append(a)

    print(" ".join(result_list))

if __name__ == "__main__":
    solve()