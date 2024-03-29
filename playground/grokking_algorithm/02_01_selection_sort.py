def get_index_of_smallest_element(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    sorted_arr = []
    while arr:
        smallest_index = get_index_of_smallest_element(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr
# %%