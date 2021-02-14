# input 9 450000
# 10000yen:x 5000yen:y 1000yen:z
# x, y, z = 4, 0, 5

def abc085c_otoshidama():
    a, b = map(int, input().split())

    x, y, z = 0, 0, a

    while z >= 0:
        while y >= 0:
            if 10000 * x + 5000 * y + 1000 * z == b:
                return [x, y, z]
            else:
                y -= 1
                x += 1
        z -= 1
        y = a - z
        x = 0
    
    return [-1, -1, -1]



if __name__ == "__main__":
    x, y, z = abc085c_otoshidama()
    print('{} {} {}'.format(x, y, z))
