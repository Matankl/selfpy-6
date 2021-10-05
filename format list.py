#this function returns the lists even numbers puts , between them and "and" before the last element
FAMILY = "matan", "gal", "liron", "heli", "ram", "ziva"


def format_list(list):
    """this function returns the lists even numbers puts , between them and "and" before the last element
    :param list: list you want to use
    :type list: list
    :return: the lists even numbers puts , between them and "and" before the last element
    :rtype: list
    LENGTH == the length of the new list
    LIST_SECOND == every even element is the list but the last one"""
    #RES == THE RESULT
    if len(list) % 2 != 0:
        return "the number of elements in the list is not even"
    else:
        LENGTH = len(list)
        LIST_SECOND = list[1: LENGTH - 1 : 2]
        RES = ", ".join(LIST_SECOND) + " and " + list[-1]
        return RES 

def main():
    #activats and print the function format_list
    print(format_list(FAMILY))

if __name__ == "__main__":
    main()



help(format_list)

