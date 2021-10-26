# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 1. A certain CS professor gives 100-point exams that are graded on the following scale
#  - 90-100: A
#  - 80-89: B
#  - 70-79: C
#  - 60-69: D
#  - <60: F
# Write a program that accepts an exam score as input and uses a decision structure to calculate the corresponding grade.

# %%
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

# %% [markdown]
# ## 2. A certain college classifies students according to credits earned.
# A student with less than 7 credits is a Freshman. At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classified as a Senior. Write a program that calculates class standing from the number of credits earned.

# %%
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

# %% [markdown]
# ## 3. A babysitter charges $2.5 an hour until 9:00PM when the rate drops to $1.75 an hour (the children are in bed)
# Write a program that accepts a starting time and ending time (in hours and minutes) and calculates the total babysitting bill. You may assume that the starting and ending times are in a single 24-hour period.

# %%
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


