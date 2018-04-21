#coding=utf-8

import random

# 
# The seed no. will be counted by WeChat automatically.
# See the article for more details.
# Here, the value 10000 and 9999 are just two examples.
#
random.seed(10000)  # If seed is 10000, the result is 5
#random.seed(9999)   # If seed is 9999, the result is 1

nums = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 2, 3, 4, 5, 6, 7, 8,
        1, 2, 3, 4, 5, 6, 7,
        1, 2, 3, 4, 5, 6,
        1, 2, 3, 4, 5,
        1, 2, 3, 4,
        1, 2, 3,
        1, 2,
        1
        ]

print random.choice(nums)
