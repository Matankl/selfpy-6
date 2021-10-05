#this function returns the lists even numbers puts , between them and "and" before the last element
FAMILY = ["matan", "gal", "liron", "heli", "ram", "ziva"]
odd_is_even = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23] # global variable
# ODD_IS_EVEN because the counting starts at 0
def format_list(list):
    #this function returns the lists even numbers puts , between them and "and" before the last element
    #NUMBER_OF_EVEN == the number of even numbers in the list that comes es argument
    #PLAY_PLACES == the places of the carecters that shuld come in the return
    global odd_is_even
    if len(list) % 2 != 0:
        return "the number of elements in the list is not even"
    else:
        NUMBER_OF_EVEN = odd_is_even[(len(list) // 2)]
        PLAY_PLACES = odd_is_even[0:NUMBER_OF_EVEN-2]

        return list[PLAY_PLACES:]

format_list(FAMILY)