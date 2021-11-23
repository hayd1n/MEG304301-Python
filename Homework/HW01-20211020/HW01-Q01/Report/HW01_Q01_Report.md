# Homework 01

## Question 1

for MEG304301

張皓鈞 B11030202



![截圖 2021-10-31 下午8.22.49](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q01/Report/Img/截圖 2021-10-31 下午8.22.49-5683053.png)



## Code

```python
# Collatz sequence
# Xi+1 = Xi/2 if Xi is even 偶數
#        3Xi+1 if Xi is odd 奇數
# Example
#  Input: X0 = 5
#  Output: 5 16 8 4 2 1

print("Collatz sequence")

print("Input X0=", end='')
x0 = int( input() )

nums = list( [ x0 ] )

i = 1
while True:
    if nums[i - 1] % 2 == 0:
        num = nums[i - 1] / 2
    else:
        num = nums[i - 1] * 3 + 1
    nums.append(num)
    i += 1
    if num == 1: break

for num in nums:
    print(int(num), end=" ")
```



## Tests & Results

```
hao@zhanghaojundeMacBook-Pro HW01-Q01 % python3 HW01-Q01.py 
Collatz sequence
Input X0=103
103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
```

![截圖 2021-10-31 下午8.27.25](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q01/Report/Img/截圖 2021-10-31 下午8.27.25.png)