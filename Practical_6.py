#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Exercise: What if you wanted just the sum column, and didn't need the original table? Write an awk command that takes a two column table and outputs just the sum column.


paste <(seq 1 5) <(seq 11 15) | awk '{$3 = $1 + $2; print $3}'


##Exercise: Write a python program stats-sum which reads a newline-separated list of floating-point numbers from standard input. When it reaches the end of standard input, it prints the sum, and exits.


#!/usr/bin/python3

import sys

sum = 0
for line in sys.stdin:
        sum += float(line)

print(sum)

##Exercise: Write similar "aggregator" programs computing stats-mean, stats-median, stats-variance, stats-stddev (standard deviation), stats-mad (median absolute deviation). Feel free to use the standard library, but do not use any third-party python packages.

mean

#!/usr/bin/python3

import sys
import statistics as s

arr = []
for line in sys.stdin:
        arr.append(float(line))

print(s.mean(arr))


median

#!/usr/bin/python3

import sys
import statistics as s

arr = []
for line in sys.stdin:
        arr.append(float(line))

print(s.median(arr))


variance

#!/usr/bin/python3

import sys
import statistics as s

arr = []
for line in sys.stdin:
        arr.append(float(line))

print(s.variance(arr))

std

#!/usr/bin/python3

import sys
import statistics as s

arr = []
for line in sys.stdin:
        arr.append(float(line))

print(s.stdev(arr))

