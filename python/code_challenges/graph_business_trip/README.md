# Code Challenge: Class 37: Graph Business Trip

## Implementation: Graph
*Author: Kevin Henry with Anthony Williams and Tony Regalado

---

## Feature Tasks:

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node
    - Arguments: value
    - Returns: The added node
    - Add a node to the graph

- add edge
    - Arguments: 2 nodes to be connected by the edge, weight (optional)
    - Returns: nothing
    - Adds a new edge between two nodes in the graph
    - If specified, assign a weight to the edge
    - Both nodes should already be in the Graph

- get nodes
    - Arguments: none
    - Returns all of the nodes in the graph as a collection (set, list, or similar)

- get neighbors
    - Arguments: node
    - Returns a collection of edges connected to the given node
        - Include the weight of the connection in the returned collection

- size
    - Arguments: none
    - Returns the total number of nodes in the graph


### NOTES:


## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

[x] 1. Node can be successfully added to the graph
[x] 2. An edge can be successfully added to the graph
[x] 3. A collection of all nodes can be properly retrieved from the graph
[x] 4. All appropriate neighbors can be retrieved from the graph
[x] 5. Neighbors are returned with the weight between nodes included
[x] 6. The proper size is returned, representing the number of nodes in the graph
[x] 7. A graph with only one node and edge can be properly returned
[x] 8. An empty graph properly returns null

Ensure your tests are passing before you submit your solution.

---

# Code Challenge: Class 36: Graph Breadth First

## Implement a breadth-first traversal on a graph

## Feature Tasks:

Write the following method for the Graph class:

- breadth first
- Arguments: Node
- Return: A collection of nodes in the order they were visited.
- Display the collection

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write at least three test assertions for each method that you define.

Ensure your tests are passing before you submit your solution.

---

### Credit & Collaboration
[Geeks for Geeks](https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/)
[Geeks for Geeks - BFS](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
[How to implement a graph in Python](https://www.educative.io/edpresso/how-to-implement-a-graph-in-python)
[Graphs 101](https://levelup.gitconnected.com/graphs-101-67581c17178d)
[How to implement a ​breadth-first search in Python](https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python)
[How to Implement Breadth-First Search (BFS) using Python](https://www.pythonpool.com/bfs-python/)

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***

---

For more information on Markdown: https://www.markdownguide.org/cheat-sheet
