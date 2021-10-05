list1 = "111", "234", "2000", "goru", "birthday", "09"

def longest(list):
    """ the function gets a list and return the longest element.
    :param list: list of strings
    :type list: lsit
    :return: the longest element
    :rtype: str"""
    list = max(list, key=len)
    return list

print(longest(list1))