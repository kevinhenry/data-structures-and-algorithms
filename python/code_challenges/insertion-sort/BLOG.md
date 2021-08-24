# Class 26 - Insertion Sort

## Pseudocode
```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
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


### Visual

| I | II|III|IV | V | VI|VII|
|---|---|---|---|---|---|---|
| 8 | 4 | 23| 42| 16| 15|Initial List|
| 4 | 8 | 23| 42| 16| 15|   |
| 4 | 8 | 23| 42| 42| 15|   |
| 4 | 8 | 16| 23| 42| 15|   |
| 4 | 8 | 16| 23| 42| 42|   |
| 4 | 8 | 16| 23| 23| 42|   |
| 4 | 8 | 16| 16| 23| 42|   |
| 4 | 8 | 15| 16| 23| 42|Sorted List|


## Code

```
sort_list = [8, 4, 23, 42, 16, 15]

def insertion_sort(sort_list):

    for i in range(1, len(sort_list)):
        print(f'I in for loop: {i}')
        key = sort_list[i]
        print(f'key in for loop: {key}')
        j = i - 1
        print(f'J in for loop: {j}\n')

        print("///While Loop Starts///\n")
        while j >= 0 and key < sort_list[j]:
          print(f'arr at start of while loop: {sort_list}')
          sort_list[j + 1] = sort_list[j]
          print(f'arr at middle of while loop: {sort_list}')
          j -= 1
          print(f'J in while loop: {j}')
        sort_list[j + 1] = key
        print(f'sort_list at end of while loop: {sort_list}')

insertion_sort(sort_list)
print ('Sorted array is:')
for i in range(len (sort_list)):
  print ("%d" %sort_list[i])
```
