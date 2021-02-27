def solve():
    n = int(input())

    x = int(n ** 0.5) + 1
    
    list_answer = []
    a = 2
    while a < x:
        y = a * a
        while y <= n:
            list_answer.append(y)
            y *= a
        a += 1
    
    print(n - len(list(set(list_answer))))
        

if __name__ == "__main__":
    solve()