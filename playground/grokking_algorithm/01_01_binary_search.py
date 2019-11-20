import math

def binary_search(ls,item):
    low = 0
    high = len(ls) -1
    while low <= high:
        mid = math.floor((low + high)/2)
        if item == ls[mid]:
            return mid
        if item < ls[mid]:
            high = mid - 1
        elif item > ls[mid]:
            low = mid + 1
    return None
# %%