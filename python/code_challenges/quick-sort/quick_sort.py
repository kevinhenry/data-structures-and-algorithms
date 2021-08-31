def quick_sort(arr, left, right):
  if (left < right):
    pivot_point = partition(arr, left, right)
    quick_sort(arr, left, pivot_point -1)
    quick_sort(arr, pivot_point + 1, right)

def partition(arr, left, right):
  pivot = arr[right]
  low = (left - 1)

  for i in range(left, right):
    if arr[i] <= pivot:
      low += 1
      swap(arr, i, low)
  swap(arr, right, low + 1)
  return (low + 1)

def swap(arr, i, low):
  temp = arr[i]
  arr[i] = arr[low]
  arr[low] = temp

arr = [8, 4, 23, 42, 16, 15]
quick_sort(arr, 0, len(arr) -1)

print(f'Sorted Array: {arr}')
