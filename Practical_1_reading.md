#Computer Architecture 

###Interlude: review of logic

Exercise: Compute the truth table for NOT:

| X| NOT X |
| --- | --- |
| 0 | 1 | 
| 1 | 1 | 

Exercise: Compute the truth table table for AND.

| X | NOT X | X and Y |
| --- | --- | --- |
| 0 | 0 | 0 | 
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Exercise: Compute the truth table for exclusive-or, defined by the formula:

XOR(X, Y) = (X OR Y) AND NOT (X AND Y)

| X | Y | (1) X AND Y | (2) X OR Y | XOR(X, Y) = (2) AND NOT (1) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

Exercise: Prove De Morgans theorem, NOT(X OR Y) = NOT(X) AND NOT(Y), 
by completing the table and checking the last two columns are the same.

| X | Y | NOT(X OR Y) | NOT(X) AND NOT(Y) |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |

Exercise: using truth tables, check these three equations
NOT(X) = NAND(1, X) = NOT(1 AND X)

|X | Y | NOT(X) | (1) 1 AND X | NOT (1) = NAND(1, X)|
| --- | --- | --- | --- | --- |
|0 | 0 | 1 | 0 | 1 |
|0 | 1 | 1 | 0 | 1 |
|1 | 0 | 0 | 1 | 0 |
|1 | 1 | 0 | 1 | 0 |


AND(X, Y) = NOT(NAND(X, Y)) = NOT(NOT(X AND Y))

| X | Y | (1) X AND Y | NOT NOT (1) = NOT(NAND(X, Y)) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |

OR(X, Y) = NAND(NOT(X), NOT(Y))) = NOT(NOT(X) AND NOT(Y))

| X | Y | (1) NOT X | (2) NOT Y | ( 1) AND (2) = NAND(NOT(X), NOT(Y))) | X OR Y |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |

Exercise: write similar formulas expressing NOT, AND, and OR in terms of NOR

NOT(X) = NOR(0,X)

| X | (1) 0 OR X | NOT (1) | NOT X |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

AND(X,Y) = NOR(NOR(0,X),NOR(0,Y)))

| X | Y | (1) NOR(0,X) | (2) NOR(0,Y) | NOR((1),(2)) | X AND Y |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 |

OR(X,Y) = NOR(NOR(0, NOR(0, X)), NOR(0, NOR(0, Y)))

| X | Y | (1) NOR(0,X) | (2) NOR(0,Y) | (3) NOR(0, (1)) | (4) NOR(0, (2)) | NOR((3), (4)) |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 |

Exercise: why NOT and OR can't be expressed in terms of AND? Explain.

Lets write a truth table and show

NOT(X) = AND(1,X)

| X | NOT(X) | AND(1,X) |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 0 | 1 |


NOT(X) = AND(0,X)

| X | NOT(X) | AND(0,X) |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 0 | 0 |

OR(X,Y) = AND(AND(0, X), AND(0, Y))

| X | Y | (1) AND(0, X) | (2) AND(0, Y) | AND((1), (2)) | OR(X, Y) |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 1 |

OR(X,Y) = AND(AND(0, X), AND(1, Y))

| X | Y | (1) AND(0, X) | (2) AND(1, Y) | AND((1), (2)) | OR(X, Y) |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 | 1 |

OR(X,Y) = AND(AND(1, X), AND(1, Y))

| X | Y | (1) AND(1, X) | (2) AND(1, Y) | AND((1), (2)) | OR(X, Y) |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 |

Binary numbers as lists of boolean values

Exercise: Without listing explicitly, how many possible 8-bit binary numbers are there?
256

Exercise: Convert X = 110 to decimal.
1 * 2^2 + 1 * 2^1 + 0 * 2^0 = 1 * 4 + 1 * 2 + 0 * 1 = 4 + 2 + 0 = 6

Exercise: Convert 11 to binary.
11 //  2 = 5 -> 11 - 10 = 1 
5 // 2 = 2 -> 5 - 4 = 1
2 // 2 = 1 -> 2 - 2 = 0
1 // 2 = 0 -> 1 - 0 = 1
Answer: 1011

Exercise: Convert these powers of 2 into binary: 2, 4, 8, 16, 32. What do you notice?

2 = 10
4 = 100
8 = 1000
16 = 10000
32 = 100000

extra bit with every power

Exercise: Convert these numbers into binary: 1, 3, 7, 15, 31 (they are all 2^n - 1 for some n). What do you notice?
1 = 1
3 = 11
7 = 111
15 = 1111
31 = 11111


Exercise: check that these numbers all have the same 3-bit representation
3 = 11 = 17
    011 = 1011 != 10001
0 = 8 = 16
    000 = 1000 = 10000
2 = 10 = 18
    010 = 1010 = 10010

##Binary arithmetic as logical operations
Exercise: complete the table by converting 2 into single-bit binary:

| X0 | Y0 | Z0 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

Exercise: do the same for single-bit multiplication: write down the table of binary numbers for X0, Y0, and the binary representation of their product Z0, and find the logical operation which matches. We say this operation implements single-bit multiplication.

| X0 | Y0 | Z0 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

##Digital Logic
Exercise: Using A and B as the inputs, and OUT as the output, explain how this circuit acts as NAND(A,B); for each entry in the truth table, follow the explanation above. True is "high energy" and False is "low energy".

| A | B | NAND(A,B) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

| A | B | NAND(A,B) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 | 
| 1 | 1 | 0 | 

1)both gates were without power, so there was a loss of power 
2)one of the gates was without power, so energy was lost 
3)oone of the gates was without power, so energy was lost
4)both gates were energized, so there was no loss of power




