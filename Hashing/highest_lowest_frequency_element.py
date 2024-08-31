# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

# Example 2:

# Input: array[] = {2,2,3,4,4,2};
# Output: 2 3
# Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
import sys

arr = [10,5,10,15,10,5]

my_dict = dict()
for i in arr:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

maxi = 0
mini = sys.maxsize

for k,v in my_dict.items():
    if v > maxi:
        maxi = k
    if v < mini:
        mini = k

print('my dict: ',my_dict)
print('maxi: ',maxi)
print('mini: ',mini)

    
