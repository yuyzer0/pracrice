
def abc189B():
    n, x = map(int, input().split())
    
    list_v, list_p = [], []

    i = 0
    while i < n:
        v, p = map(int, input().split())
        list_v.append(v)
        list_p.append(p)
        i += 1
    
    i = 0
    alc = 0
    while i < n:
        alc += list_v[i] * list_p[i]
        if alc > x * 100:
            print("{}".format(i + 1))
            return
        else:
            i += 1

    print(-1)
    return

if __name__ == "__main__":
    abc189B()