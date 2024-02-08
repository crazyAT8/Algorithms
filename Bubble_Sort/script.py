def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                # Swap elements
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1  # Reduce the range by 1 because the last element is in its rightful place
        if not swapped:
            break  # If no two elements were swapped by the inner loop, then the list is sorted
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))


''''''
# .khvb;khbkbkljn
''''''
