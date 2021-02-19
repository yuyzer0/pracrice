
def abc190_very_very_primitive_game():
   list_num = [int(s) for s in str(input()).split()]
   if list_num[2] == 0:
        if list_num[0] - list_num[1] > 0:
            print("Takahashi")
        else:
            print("Aoki")
   else:
        if list_num[1] - list_num[0] > 0:
            print("Aoki")
        else:
            print("Takahashi")


if __name__ == "__main__":
    abc190_very_very_primitive_game()