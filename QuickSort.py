def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left) + [pivot] + quicksort(right)
nums=[1,4,5,6,4,6,7]
print(quicksort(nums))
