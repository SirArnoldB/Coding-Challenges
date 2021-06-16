from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Solution 1: Hash Table : O(n) - time | O(n) - space
        ----------
        '''
        """
        Algorithm:
        ---------
        - Iterate through all the elements in nums, 
        - set up key/value pair. 
        - return the element which appeared only once
        """
        numsMap = defaultdict(int)
        for num in nums:
            numsMap[num] += 1

        for num, value in numsMap.items():
            if value == 1:
                return num
            
'''
Solution 2: Math : O(n) - time | O(n) - space
-----------
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Idea: 2∗(a+b+c)−(a+a+b+b+c)=c
        '''
        return 2 * sum(set(nums)) - sum(nums)

'''
Solution 3: Bit Manipulation: O(n) - time | O(1) - space
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        ## Idea:
        - If we take XOR of zero and some bit, it will return that bit
            >>> a⊕0=a
        - If we take XOR of two same bits, it will return 0
            >>> a⊕a=0
        >>> a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        
        '''
        a = 0
        for i in nums:
            a ^= i
        return a