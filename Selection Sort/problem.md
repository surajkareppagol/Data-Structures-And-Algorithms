# Selection Sort

`Selection Sort` takes a list of items and sorts them in ascending order, the time complexity is `O(n ^ 2)`.

The main working principle here is that, you check entire list find the `smallest` (here i am checking for smaller, you can check for larger item) item, then add it into `new list`.

Then again check the list, find the `smallest` item and add it into `new list` repeat this same procedure until the list gets sorted.

Here `find_smallest()` returns the smallest item index.
