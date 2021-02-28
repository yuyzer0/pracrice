def solve():
    n = int(input())

    while n % 2 == 0:
        n = n / 2
    
    sq = int (n ** 0.5)
    
    i = 1
    cnt = 0
    while i <= sq:
        if n % i == 0:
            cnt += 2
        if i * i == n:
            cnt -= 1
        i += 1
    
    print(cnt * 2)
    

if __name__ == "__main__":
    solve()