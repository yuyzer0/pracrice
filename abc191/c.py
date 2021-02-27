def solve():
    h, w = map(int, input().split())

    i = 0
    s = []
    while i < h:
        sw = str(input())
        s.append(sw)
        i += 1
    
    i = 0
    cnt = 0
    while i < h - 1:
        j = 0
        while j < w -1:
            if judge(s, i, j):
                cnt += 1
            j += 1
        i += 1
    
    print(cnt)

def judge(sw: list, i: int, j: int) -> bool:
    list_s = [str(s) for s in sw[i]]
    list_s_after = [str(s) for s in sw[i+1]]
    
    list_judge = [list_s[j], list_s[j+1], list_s_after[j], list_s_after[j+1]]
    cnt = list_judge.count("#")

    if cnt == 1 or cnt == 3:
        return True
    else:
        return False

if __name__ == "__main__":
    solve()