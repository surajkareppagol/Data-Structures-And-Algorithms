def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    result_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        result_arr.append(arr.pop(smallest))
    return result_arr


input_arr = [3, 4, 1, 6, 2, 5]

print(selection_sort(input_arr))
