def b():
    n = int(input())
    s = str(input())

    count = 0
    repS = s
    while not(repS == s.replace("ABC", '')):
        repS = s.replace("ABC", '', count + 1)
        count += 1
    
    print(count)

if __name__ == "__main__":
    b()