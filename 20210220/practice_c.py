def c():
    n , k = map(int, input().split())

    i = 0
    while i  < k:
        g1 = sorted(list([s for s in str(n)]))
        g2 = sorted(g1, reverse = True)
        int_g1 = int(''.join(g1))
        int_g2 = int(''.join(g2))
        n = int_g2 - int_g1
        i += 1
    
    print(n)

if __name__ == "__main__":
    c()