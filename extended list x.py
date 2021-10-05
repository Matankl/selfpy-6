LIST_Y = 1, 2, 3, 4, 5, 6, 7, 8, 9
list_x = 'a', "b", "c", "d", "e" ,"f" ,"g", "h" ,"i"

def extend_list_x(LIST_X = list_x, LIST_Y = LIST_Y):
    """this function combine list x in list y (list y first) and print it
:param LIST_X: list you want to be second
:type LIST_X: list
:param LIST_Y: list you want to be first
:type LIST_Y: list
:return:LIST_X = LIST_Y + LIST_X printed
:rtype: list"""
    global list_x
    list_x = *LIST_Y , *LIST_X
    return print(list_x)

help(extend_list_x)

def main():
    extend_list_x()

if __name__ == "__main__":
    main()


