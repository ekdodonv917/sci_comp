##Data Representation I

##Numerical representations

Binary and hexadecimal representations

Exercise: build a list of all four-digit binary numbers, and compute the corresponding single-digit hexadecimal number.

| four-digit binary numbers | single-digit hexadecimal number |
| --- | --- |
| 0000 | 0 |
| 0001 | 1 |
| 0100 | 2 |
| 0011 | 3 |
| 0010 | 4 |
| 0111 | 5 |
| 0110 | 6 |
| 0101 | 7 |
| 1000 | 8 |
| 1001 | 9 |
| 1011 | A |
| 1010 | B |
| 1101 | C |
| 1100 | D |
| 1110 | E |
| 1111 | F |

Exercise: Pretend we use a naïve floating-point format with 5bit mantissa and 3bit exponent (base-2). What is the smallest possible positive number representable? What is the largest positive number representable?

##Simple data structures: lists, trees, graphs

Linked lists

Exercise: use diagrams like the above to explain how to delete an item from a linked list.

| x[0] | next |--->---| x[1] | next |--->---| x[2] | NULL |

After

| x[0] | next |--->---|--->---| x[2] | NULL |

###Trees
Exercise: assemble the numbers 1-10 into binary search trees which are (a) maximally unbalanced to the left, (b) balanced, (c) one step from balanced.

a) maximally unbalanced to the left



```python
                  10
                  /
                 9
                /
               8
              /
             7
            /
           6
          /
         5
        /
       4
      /
     3
    /
   2
  /
 1
```

b) balanced


```python
         5
      /     \
     3       8
    / \     / \
   2   4   7   9
  /       /     \
 1       6       10
```

c) one step from balanced.


```python
       4
    /     \
  2         6
/   \      /  \
1     3    5    8
               / \
              7   9
                   \
                    10
```

##Graphs
###Exercise: assemble a directed acyclic graph with the numbers 1-12 by strict divisibility: an edge from A to B if B/A is prime. There are no directed cycles, but some nodes do have multiple paths to them. (These form cycles if you ignore the direction.) Which ones? Explain how to decide if a number will have multiple paths to it.

              5    7 ->- 10       3
               ↖  ↗     ↗       ↗
         12 -<-  1  ->- 2  ->- 4
                  ↘      ↘      ↘
              9 -<- 8 ->- 6 ->-  11


6, 10, 12 - Multiple paths due to the fact that they are devisable by two prime numbers

###Exercise: Identify several maximal spanning trees in the divisibility graph from the previous exercise.

1 -> 2 -> 4 -> 3
1 -> 3 -> 6 -> 11
1 -> 2 -> 4 -> 11


###Exercise: model acquaintance using a graph (vertices are people, an edge between A and B means A knows B). Model it with a directed graph. How are these different?

Graph allowed only oneway edges, acquaintance assumes that A and B can know each other -- > possible cycles .
