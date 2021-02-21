
def a():
    x = int(input())

    i = 0
    while True:
        if (x + i) % 100 == 0 and i > 0:
            print("{}".format(i))
            return
        else:
            i += 1
        
    

if __name__ == "__main__":
    a()