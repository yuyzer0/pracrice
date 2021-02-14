def abc085b_kagamimochi():
    
    n = int(input())

    i = 0
    list_a = []
    
    while i < n :
        list_a.append(int(input()))
        i += 1
    
    print(len(list(set(list_a))))

if __name__ == "__main__" :
    abc085b_kagamimochi()
