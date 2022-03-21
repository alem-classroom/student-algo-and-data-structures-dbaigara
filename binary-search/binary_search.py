def binary_search(lst, to_find):
    if to_find in lst:
        return lst.index(to_find)
    else:
        return -1
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1