def a():
    list_in = [int(s) for s in str(input()).split()]
    v = list_in[0]
    t = list_in[1]
    s = list_in[2]
    d = list_in[3]

    if v * t > d or v * s < d:
        print("Yes")
    else:
        print("No")
    
    return

if __name__ == "__main__":
    a()