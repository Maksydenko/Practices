import numpy as np
import random

# Task 1

nums = np.random.randint(-10, 10, 10)
value = randint(-10, 10)
i = 0

while i < len(nums) and nums[i] != value:
    i += 1

if i == len(nums):
    print("Element not found")
else:
    print("Element", value, "found at position", i)
print("Number of matches according to the skin algorithm:", i)

# Task 2

nums = sorted(np.random.randint(-10, 10, 10))
value = randint(-10, 10)
i = -1
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] > value:
        right = mid - 1
    elif nums[mid] < value:
        left = mid + 1
    else:
        i = mid
        break

if i == -1:
    print("Element not found")
else:
    print("Element", value, "found at position", i)
print("Number of matches according to the skin algorithm:", i)

# Task 3

text = "Hello, world!"
pattern = "world"
i = -1
j = 0

while j < len(pattern) and i < (len(text) - len(pattern)):
    j = 0
    i += 1

    while j < len(pattern) and pattern[j] == text[i + j]:
        j += 1

if j == len(pattern):
    print("Substring found at position", i)
else:
    print("Substring not found")
print("Number of matches according to the skin algorithm:", i + j)
