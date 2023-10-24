def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        search = arr[mid]

        if search == item:
            return mid
        elif search > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


input_arr = [1, 2, 3, 4, 5, 6]

print(binary_search(input_arr, 5))
