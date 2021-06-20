'''
Find The Duplicate Number
------------------------
Source: https://leetcode.com/problems/find-the-duplicate-number/
'''
"""
Solution 1 : Floyd's Tortoise and Hare (Cycle Detection)
"""

'''
>>> The idea is to reduce the problem to a Linked List Cycle
    >>> Given a linked list, return the node where the cycle begins

>>> First of all, where does the cycle come from? 
>>> Let's use the function f(x) = nums[x] to construct the sequence: 
    >>> x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....
    
    >>> Each new element in the sequence is an element in nums at the index of the previous element.

>>> If one starts from x = nums[0], such a sequence will produce a linked list with a cycle.
    >>> The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.
    
>>> Now the problem is to find the entrance of the cycle.

### Algorithm
>>> Floyd's algorithm consists of two phases and uses two pointers usually called tortoise and hare. 

# Phase 1:
>>> In phase 1, hare = nums[nums[hare]] is twice as fast as tortoise = nums[tortoise]. 
>>> Since the hare goes fast, it would be the first one who enters the cycle and starts to run around the cycle. >>> At some point, the tortoise enters the cycle as well, and since it's moving slower the hare catches the 
>>> tortoise up at some intersection point. Now phase 1 is over, and the tortoise has lost.

    >>> Note that the intersection point is not the cycle entrance in the general case.

>>> To compute the intersection point, let's note that the hare has traversed twice as many nodes as the         >>>> tortoise, i.e. 2d(tortoise) = d(hare), that means

    # 2(F + a) = F + nC + a2(F+a)=F+nC+a, where nn is some integer.
    # Hence the coordinate of the intersection point is F + a = nCF+a=nC.
 
# Phase 2:
>>> In phase 2, we give the tortoise a second chance by slowing down the hare, so that it now moves with the 
>>> speed of tortoise: tortoise = nums[tortoise], hare = nums[hare]. 
>>> The tortoise is back at the starting position, and the hare starts from the intersection point.

>>> Let's show that this time they meet at the cycle entrance after F steps.

    >>> The tortoise started from zero, so its position after FF steps is F.

    >>> The hare started at the intersection point F + a = nC, so its position after F steps is nC + +F, that is         the same point as F.

    >>> So the tortoise and the (slowed down) hare will meet at the entrance of the cycle.  

### Implementation
'''
# O(n) - time | O(1) - space: where n is the length of nums
# Also check out: Linked List Cycle II. 
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

# ********************************************************************************************* # 

"""
Solution 2 : Sorting
"""
# O(nl log n) - time | O(1) - space
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        """
        Proving that at least one duplicate must exist in nums is simple application of the pigeonhole principle.         Here, each number in nums is a "pigeon" and each distinct number that can appear in nums is a                     "pigeonhole". Because there are n+1n+1 numbers are nn distinct possible numbers, the pigeonhole principle         implies that at least one of the numbers is duplicated.
        """
        # sort the numbers in place; O(nlogn) - time 
        # If the numbers are sorted, then any duplicate numbers will be adjacent in the sorted array.
        nums.sort() 
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return nums[i]
            i += 1

# ********************************************************************************************* # 
         
"""
Solution 3 : Using a Set 
"""
# O(n) - time | O(n) - space
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
           
        seen = set()
        for num in nums:
            if num in seen:
                return num
            set.add(num)
            