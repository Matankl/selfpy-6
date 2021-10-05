list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

def are_lists_equal(list1 = list1, list2 = list2):
    """this function gets 2 str or int lists and return True if they contain same elements
    :argument list1: first list to compare
    :type list1: list
    :argument list2: second list to compare
    :type list2: list
    :return: True if lists containe same elements False if not
    :rtype: bool"""
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

if __name__ == "__main__":
    are_lists_equal()

