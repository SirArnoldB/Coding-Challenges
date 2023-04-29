---
description: Three Sum Problem
---

# 🚀 3Sum

**Source: [Leetcode](https://leetcode.com/problems/3sum/)**

{% tabs %}
{% tab title="Problem Statement" %}

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1:

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.
```

### Example 2:

```

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

### Example 3:

```

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

### Constraints:

```

3 <= nums.length <= 3000

-105 <= nums[i] <= 105

```

{% endtab %}

{% tab title="Solution 1 Walkthrough" %}

# Intuition

> The problem requires finding all the unique triplets that sum up to zero. A brute-force approach would require three nested loops, which would result in a time complexity of `O(n^3)`. However, we can optimize the solution by sorting the array first and then applying a two-pointer approach. This reduces the time complexity to `O(n^2)`.

# Approach

> Firstly, we `sort` the input array. After sorting, we can use a pointer at the start and another at the end of the array. We then use a third pointer, which we will call the `middle` pointer, which starts at the position of the first pointer plus one.

> We iterate through the array with the first pointer, `i`, until the third-last element, as we require at least two elements after `i` to form a triplet. Inside this loop, we initialize our `middle` and `end` pointers to `i+1 `and `len(nums)-1` respectively.

> While the second pointer is less than the third pointer, we calculate the `sum` of the three numbers at these pointers. If the sum is `zero`, we append the triplet to our output list and increment the second pointer and decrement the third pointer. We then update the second pointer by skipping over any duplicate values, and the third pointer by skipping over any duplicate values.

> If the sum is less than `zero`, we increment the second pointer, since increasing the value at the second pointer increases the sum.

> If the sum is greater than `zero`, we decrement the third pointer, since decreasing the value at the third pointer decreases the sum.

> We also check for duplicate values at the start pointer by comparing it to its previous value.

# Complexity

- Time complexity: `O(n^2)`

  > Sorting takes `O(nlogn)` time, and we use a two-pointer approach, which takes `O(n)` time. Therefore, the overall time complexity is `O(nlogn + n^2) = O(n^2)`.

- Space complexity: `O(1)`
  > We use constant space for storing pointers and variables, and we do not create any new data structures. Therefore, the space complexity is `O(1)`.

# Code

{% code lineNumbers="true" %}

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif three_sum < 0:
                    left += 1

                else:
                    right -= 1

        return triplets

```

{% endcode %}

{% endtab %}
