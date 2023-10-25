# Binary Search

`Binary Search` algorithm makes searching faster. Compared to `Linear Search` it is much more faster, the time complexity is `O(log n)`.

It needs a `Sorted List` and an `Item` to search as input, if it founds the item it returns the position of that item from the list, or else it returns `None`.

The working of binary search is simple.

![Binary Search](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/binarySearch_1.png)

Here the list has 6 items, and the item to search is `5`. Set `low = 0` and `high = len(arr) - 1`.

```python
low = 0
high = len(arr) - 1
```

Calculate `mid` as,

```python
mid = (low + high) // 2
```

Here `low = 0` and `high = 5`, so `mid = 2`. So now search for mid position in the list, the `item` will be `3` and it is not equal to the search item.

```python
if search == item:
  return mid
elif search > item:
  high = mid - 1
else:
  low = mid + 1
```

Since here `3` is less than `item` to be searched it will be under `else`, where `low = mid + 1`, i.e `low = 3`.

![Binary Search](https://raw.githubusercontent.com/surajkareppagol/assets-for-projects/main/binarySearch_2.png)

Again calculate `mid`, now it will be `4`, and the `item` will be `5`, it is equal to the `item` to be searched so it will return `mid` value that is `4`.
