# input 
# 3
# 8 12 40

# 1 : 4 6 10
# 2 : 2 3 5

num = int(input())
str_a = str(input())
list_a = str_a.split()

count = -1
flg = True
i = 0

while flg:
    i = 0
    for a in list_a :
        if int(list_a[i]) % 2 == 1:
            flg = False
            break
        else :
            list_a[i] = int(int(list_a[i]) / 2)
        i += 1
    count += 1

print(count)     

