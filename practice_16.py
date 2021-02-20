
def abc189A():
    list_c = [str(s) for s in str(input())]
    
    if list_c[0] == list_c[1] and list_c[1] == list_c[2]:
        print("Won")
    else:
        print("Lost")

if __name__ == "__main__":
    abc189A()