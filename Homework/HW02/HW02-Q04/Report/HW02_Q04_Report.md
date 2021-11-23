# Homework 02

## Question 4

for MEG304301

張皓鈞 B11030202

![截圖 2021-11-24 上午1.19.54](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW02/HW02-Q04/Report/Img/截圖 2021-11-24 上午1.19.54.png)

### Key Part Code

```python
import random

X_POS_LIMIT = 1000
Y_POS_LIMIT = 1000

deliverers_name = ["甲外送員", "乙外送員", "丙外送員"]
deliverers = list()
def genDeliveries(deliverers_name):
    for name in deliverers_name:
        deliverers.append( {
            "name": name,
            "pos": {
                "x": random.randint(X_POS_LIMIT * -1, X_POS_LIMIT),
                "y": random.randint(Y_POS_LIMIT * -1, Y_POS_LIMIT)
            }
        } )
genDeliveries(deliverers_name)
```

### Results Screehsots

![截圖 2021-11-24 上午1.24.43](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW02/HW02-Q04/Report/Img/截圖 2021-11-24 上午1.24.43.png)

![截圖 2021-11-24 上午1.25.13](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW02/HW02-Q04/Report/Img/截圖 2021-11-24 上午1.25.13.png)

![截圖 2021-11-24 上午1.25.53](/Users/hao/Documents/GitHub/MEG304301-Python/Homework/HW02/HW02-Q04/Report/Img/截圖 2021-11-24 上午1.25.53.png)

### 說明

可以看見，一開始先宣告deliverers_name陣列存放外送員名單，然後利用genDeliverers()函數按名單產生外送員的完整資訊，其中的for迴圈遍歷整個deliverers_name陣列，並在新的deliverers陣列中append完整資訊的dict，其中包括name及pos資訊

### 心得

使用Python Tutor可以很方便的的將程式運行的過程具象化，並且把執行的過程逐幀拆解，可以很方便的對程式進行偵錯，也可以快速了解程式對於資料的管控及操作，是相當方便的工具。
