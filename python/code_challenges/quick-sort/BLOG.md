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

## Algorithm

     `InsertionSort(int[] arr)`
*Define a function that takes in a list of integers*

    `FOR i = 1 to arr.length`
*Starts a for loop that will loop through the array starting at index 1 and going the length of the array*

      `int j <-- i - 1`
*Creates the variable "j" and assigns it the value of 1*

      `int temp <-- arr[i]`
*Creates a temp variable and assigns it the value of the array  at index "i"*

      `WHILE j >= 0 AND temp < arr[j]`
*Creates a while loop that continues to run while variable "j" is greater than or equal to 0 AND the temp variable is less than the array at index "j"*

      `arr[j + 1] <-- arr[j]`
*Temp variable is less than array at index "j" and moves 1 index to the right in order for array to sort properly*

      `j <-- j - 1`
*Decrements variable "j"*

      `arr[j + 1] <-- temp`
*Assigns the temp variable at array at index j+1*

*Continues until it goes through the whole array

## Trace

Sample Array: [8, 4, 23, 42, 16, 15]


###
[8, 4, 23, 42, 16, 15]
15 Pivot point
8 < 15
Nothing happens
4 < 15
Nothing happens
23 > 15
Swap
15 < 23

[8, 4, 15, 42, 16, 23]
15 Pivot point
15 < 42
Nothing happens
15 < 16
*15 Locked*

[8, 4, 15, 42, 16, 23]
4 Pivot point
8 > 4
Swap
Compare 4 </> 4
*4 Locked*
Compare 8 </> 8
*8 Locked*

[4, 8, 15, 42, 16, 23]

[4, 8, 15][42, 16, 23]
23 Pivot point
42 > 23
Swap
23 < 42
23 > 16
Swap
16 < 23, 42
*23 Locked*
Compare 16 </> 16
*16 Locked*
Compare 42 </> 42
*42 Locked*


[4, 8, 15, 16, 23, 42]
>>

>>>>


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
          