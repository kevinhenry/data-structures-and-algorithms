# Daily Code Challenge README

## Implementation: Hashmap Tree Intersection
*Author: Kevin Henry with Anthony Williams, Tony Regalado, Garfield Grant

---

## Hash Table Class Methods:

- add
    - Arguments: key, value
    - Returns: nothing
    - This method should has the key, and add the key and value pair to the table, handling collisions as needed.

- get
    - Arguments: key
    - Returns: Value associated with that key in the table

- contains
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already

- hash
    - Arguments: key
    - Returns: Index in the colleciton for that key

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

[ ] Adding a key/value to your hashtable results in the value being in the data structure
[ ] Retrieving based on a key returns the value stored
[ ] Successfully returns null for a key that does not exist in the hashtable
[ ] Successfully handle a collision within the hashtable
[ ] Successfully retrieve a value from a bucket within the hashtable that has a collision
[ ] Successfully hash a key to an in-range value

---

### Whiteboard Visual
***[Hashmap Tree Intersection]***

![hashmap-tree-intersection](https://github.com/kevinhenry/data-structures-and-algorithms/blob/main/python/code_challenges/img/hashmap_tree_intersection.jpg)

---

### Credit & Collaboration
Geeks for Geeks

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***

---

For more information on Markdown: https://www.markdownguide.org/cheat-sheet
