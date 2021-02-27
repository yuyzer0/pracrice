def solve():
    a, b = map(int, input().split())
    discout = ((a - b) / a ) * 100
    print(discout)

if __name__ == "__main__":
    solve()