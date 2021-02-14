# 入力値
num = int(input())
# 入力値を文字列にして、文字列から１文字ずつリストにする
list_num = [int(s) for s in str(num)]

count = 0

for x in list_num:
    if x == 1:
        count += 1

print(count)