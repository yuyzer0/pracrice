def a():
    k = int(input())
    cnt = 0
    a, b, c = k, 1, 1
    while a > 0:
        bc = int(k/a)
        b = bc
        while b > 0:
            x = int(bc/b)
            c = x
            while c > 0:
                if a >= b and b >= c and a * b * c <= k:
                    if a == b and b == c:
                        cnt += 1
                    elif a == b and not(b == c):
                        cnt += 3
                    elif not(a == b) and b == c:
                        cnt += 3
                    else:
                        cnt += 6 
                c -=1
            b -=1
        a -= 1

      
    
    print(cnt)

if __name__ == "__main__":
    a()