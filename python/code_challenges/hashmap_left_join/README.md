# Daily Code Challenge README

## Implementation: Hashmap Left Join
*Author: Kevin Henry with Anthony Williams and Tony Regalado

---

## Feature Tasks:

Write a function that LEFT JOINs two hashmaps into a single data structure.

- Write a function called left join
- Arguments: two hash maps
    - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

### NOTES:

- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
- If no values exist in the right hashmap, then some flavor of `NULL` should be appended to the result row.

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

---

### Whiteboard Visual
***[Hashmap Left Join]***

![hashmap-left-join](https://github.com/kevinhenry/data-structures-and-algorithms/blob/main/python/code_challenges/img/hashmap_left_join.jpg)

---

### Credit & Collaboration
Geeks for Geeks

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***

---

For more information on Markdown: https://www.markdownguide.org/cheat-sheet
