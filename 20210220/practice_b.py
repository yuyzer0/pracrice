
def b():
    s = str(input())

    i = 1
    for char in s:
        if i % 2 == 0 and char == char.upper():
            i += 1
        elif i % 2 == 1 and char == char.lower():
            i += 1
        else:
            print("No")
            return
    
    print("Yes")
    return

if __name__ == "__main__":
    b()