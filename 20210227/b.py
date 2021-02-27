def solve():
    n = int(input())
    
    i = 0
    list_apx = []
    while i < n:
        str_apx = str(input())
        list_apx.append(str_apx)
        i += 1
    
    mount = 10 ** 9 + 1
    for apx in list_apx:
        list_apx_1 = [int(s) for s in apx.split()]
        x  = hantei(list_apx_1)
        if x > 0 and x < mount:
            mount = x

    if mount == 10**9 + 1:
        print(-1)
    else:
        print(mount)

def hantei(apx: list) -> int:
    zaiko = apx[2] - apx[0]
    if zaiko > 0:
        return apx[1]
    else:
         return -1
            

if __name__ == "__main__":
    solve()