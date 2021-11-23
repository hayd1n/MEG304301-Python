# Homework 01

## Question 3

for MEG304301

張皓鈞 B11030202



![截圖 2021-10-31 下午8.38.08](/Users/hao/Documents/截圖/截圖 2021-10-31 下午8.38.08.png)

## Code

```python
import math

# This is how you create a list in Python.
scores = []

# Prompt the user to enter the scores.
print("Please enter your test scores, ending the list with a -1.")

# Read in the scores.
while True:

    # Get next score.
    try:
        curscore = int(input(""))
        # Adds a value to the end of a list.
        scores.append(curscore)
        if curscore == -1: break
    except ValueError:
        print("ERROR. Reason: Wrong Type! Just input number type.")

# Set up my accumuators.
total = 0
minimum = scores[0]
maximum = scores[0]

# Go through each score.
for i in range(len(scores)):

    # Add into our total.
    total += scores[i]

    # Update the minimum if necessary.
    if scores[i] < minimum:
        minimum = scores[i]

    # Do the same for the maximum.
    if scores[i] > maximum:
        maximum = scores[i]

# Store average.
avg = total/len(scores)

# Use Python's Prewritten functions.
# print("Min is",min(scores),"Max is",max(scores),"Sum is",sum(scores))
print( "Min is {}, Max is {}, Sum is {}".format( min(scores), max(scores), sum(scores) ) )

# Print out our stats so far.
# print("Min =",minimum,"Max =",maximum,"Avg =",total/len(scores))
print( "Min = {}, Max = {}, Avg = {}".format( minimum, maximum, total / len( scores ) ) )

# Add up the sum of terms for the variance.
varsum = 0
for x in scores:
    varsum += ( ( x - avg ) ** 2 )

# Print out the standard deviation.
print( "The standard deviation is {}".format( math.sqrt( varsum / len( scores ) ) ) )
```

## Tests & Results

```
hao@zhanghaojundeMacBook-Pro HW01-Q03 % python3 HW01-Q03.py 
Please enter your test scores, ending the list with a -1.
1
2
3
4
5
6
7
8
9
10
-1
Min is -1, Max is 10, Sum is 54
Min = -1, Max = 10, Avg = 4.909090909090909
The standard deviation is 3.3153786416019035
```

![截圖 2021-10-31 下午8.39.52](/Users/hao/Library/Application Support/typora-user-images/截圖 2021-10-31 下午8.39.52.png)