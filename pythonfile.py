# 1.	Print numbers from 1 to 10 using a for loop
from os import remove

for each in range(1,11):
    print(each)


# ============================================================================================
# 2.	Calculate the sum of numbers from 1 to 10 using a for loop

total = 0

for i in range(1, 11):
    total += i  # same as total = total + i

print("The sum of numbers from 1 to 10 is:", total)


# ==========================================================================================

# 3.	Print the elements of a list using a for loop
my_list = [1,2,3,4,5,6,7,8,9]

for each in my_list:
    print(each)
