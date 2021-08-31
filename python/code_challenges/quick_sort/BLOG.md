# CC Class 28 - Quick Sort

## Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Intro

Quick sort is a devide and conguer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. The key process in quick-sort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in a sorted array and put all smaller elements before x, and put all greater valued elemtns after x.


## Trace

![quick-sort](https://github.com/kevinhenry/data-structures-and-algorithms/blob/main/python/code_challenges/img/quick-sort.jpg)


## Code

```
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
```
