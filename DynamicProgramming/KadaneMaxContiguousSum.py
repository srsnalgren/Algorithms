# PROBLEM: Find the max contiguous sum
# SOLUTION: Using Kadane's algorithm

import random

# Generate a random list of numbers
nums = random.sample(range(-1000, 1001), 10)

# Initialise the running sum and max sum
runningSum = 0
maxSum = 0

for n in nums: # Complexity: O(n)   :OOOOO
  runningSum = max(runningSum + n, 0) # Reset to 0 anytime the algebraic sum gets smaller
  maxSum = max(runningSum, maxSum) # The highest running sum we've seen

print('The list is\n', nums)
print('The maximum contiguous sum is {}'.format(maxSum))
