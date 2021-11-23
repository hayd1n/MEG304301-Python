# Homework 01

## Question 5

for MEG304301

張皓鈞 B11030202



![截圖 2021-10-31 下午9.05.13](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q05/Report/Img/截圖 2021-10-31 下午9.05.13.png)

![截圖 2021-10-31 下午9.05.38](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q05/Report/Img/截圖 2021-10-31 下午9.05.38.png)

計算出身分證字號後8碼完全相同的可能組合



## Code

### 計算校驗符

```python
def getSum(first_char_num:int, sex: int) -> int:
    num_a = int(str(first_char_num)[0:1])
    num_b = int(str(first_char_num)[1:2])
    num_c = sex
    return ( ( num_a * 1 ) + ( num_b * 9 ) + ( num_c * 8 ) ) % 10
```

### 比對所有組合

```python
for boy_first_char, boy_first_char_num in first_char_list.items():
    boy = getSum(boy_first_char_num, 1) # 夫
    for girl_first_char, girl_first_char_num in first_char_list.items():
        girl = getSum(girl_first_char_num, 2) # 妻
        if boy == girl: best_match_list[boy_first_char].append(girl_first_char)
```

### 打印配對結果

```python
pprint(best_match_list)
```

## Tests & Results

![截圖 2021-10-31 下午9.08.44](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW01-20211020/HW01-Q05/Report/Img/截圖 2021-10-31 下午9.08.44.png)
