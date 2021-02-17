
def abc191_a():
    s = str(input())
    list_s = [int (t) for t in s.split()]
    
    if list_s[0] * list_s[1] <= list_s[3] and list_s[0] * list_s[2] >= list_s[3]:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    abc191_a()