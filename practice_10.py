# input s = erasedream
# t = erase + dream
# s = t

# input s = dreameraser
# t = dream eraser

# input s = dreamer
# input 

def abc049c_daydream():
    s = str(input())

    a, b, c, d = "dream", "dreamer", "erase", "eraser"

    s = s.replace(d, '').replace(c, '').replace(b, '').replace(a, '')

    if len(s) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    abc049c_daydream()

