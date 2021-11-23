# Homework 01

## Question 4

for MEG304301

張皓鈞 B11030202



## First Question

![截圖 2021-10-31 下午8.50.23](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.50.23.png)

### Code

```python
try:
    score = int( input() )
except ValueError:
    print("錯誤！ 原因：請輸入數字。")

if score:
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = 'C'
    elif score >= 60 and score <= 69:
        grade = 'D'
    elif score < 60:
        grade = 'F'
    else:
        grade = 'Unknow'

    print( "你的成績 {} 為 {} 評級".format( score, grade ) )
```

### Tests & Results

#### Input 74

![截圖 2021-10-31 下午8.53.15](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.53.15.png)

#### Input 98

![截圖 2021-10-31 下午8.53.49](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.53.49.png)

#### Input 65

![截圖 2021-10-31 下午8.54.15](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.54.15.png)

## Second Question

![截圖 2021-10-31 下午8.55.26](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.55.26.png)

### Code

```python
print("請輸入您的點數(credits)")
try:
    credits = int( input() )
except ValueError:
    print("錯誤！ 原因：請輸入數字")

if credits:
    if credits < 7:
        level = 'Freshman'
    elif credits >= 7 and credits < 16:
        level = 'Sophomore'
    elif credits >= 16 and credits < 26:
        level = 'Junior'
    elif credits >= 26:
        level = 'Senior'
    else:
        level = 'Unknow'
    print( "你的點數(credits) {} 為 {} ".format(credits, level) )
```

### Tests & Result

#### Input 7

![截圖 2021-10-31 下午8.56.59](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.56.59.png)

#### Input 17

![截圖 2021-10-31 下午8.57.30](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.57.30.png)

#### Input 30

![截圖 2021-10-31 下午8.58.10](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.58.10.png)

## Third Question

![截圖 2021-10-31 下午8.59.09](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午8.59.09.png)

### Code

```python
normal_price = 2.5
rate_drops_price = 1.75
rate_drops_time_hours = 21

try:
    print("請輸入開始時間(時)")
    start_hours = int( input() )
    if start_hours > 24: raise ValueError()
    print("請輸入開始時間(分)")
    start_mins = int( input() )
    if start_mins > 60: raise ValueError()
    print("請輸入結束時間(時)")
    end_hours = int( input() )
    if end_hours > 24: raise ValueError()
    print("請輸入結束時間(分)")
    end_mins = int( input() )
    if end_mins > 60: raise ValueError()

    # 如果超出1分鐘，則進位1小時
    if start_mins > 0: start_hours += 1
    if end_mins > 0: end_hours += 1
    if start_hours > 24 or end_hours > 24: raise ValueError()
except ValueError:
    print("錯誤！ 原因：請輸入正確格式")

bill = 0
bill += ( end_hours - start_hours ) * normal_price
if end_hours >= rate_drops_time_hours:
    bill -= ( end_hours - max( start_hours, rate_drops_time_hours ) + 1 ) * ( normal_price - rate_drops_price )
print(bill)
```

### Tests & Results

#### Input 2:00 to 23:00

![截圖 2021-10-31 下午9.03.27](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q04/Report/Img/截圖 2021-10-31 下午9.03.27.png)