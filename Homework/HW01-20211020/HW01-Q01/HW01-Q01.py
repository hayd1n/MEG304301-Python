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