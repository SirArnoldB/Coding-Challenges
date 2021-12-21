"""
First Duplicate Value
---------------------
Source : https://www.algoexpert.io/questions/First%20Duplicate%20Value
"""
'''
Solution 1: Using a Hashmap
'''
# O(n) - time | O(n) - space : where n is the length of the input array
def firstDuplicateValue(array):
    '''
    ## Algorithm:
    -------------
    
    - create a numsMap, to store all the numbers that we have seen
    - loop through the array, 
    - when we see a number that already exists, we return that number
    '''
    numsMap = {}
    for num in array:
        if num in numsMap:
            return num
        numsMap[num] = True
    return -1

'''Solution 3: Optimal Solution 
'''
# O(n) - time | O(1) - space
def firstDuplicateValue(array):
    # since the integers are between 1 and length of the input array, 
    # we can map them to indices in the array itself by subtracting 1 from them
    # once an integer has been mapped to an index in the array, mutate the value 
    # in the array at that index and make it negative by multiplying it by -1. 
    # Since the integers normally aren't negative, the first time that we encounter a negative value at the index
    # that an integer maps to, we would have already seen that integer
    
    for value in array:
        # get the absolute value
        absValue = abs(value)
        # the value at the index that represents this value is negative
        # we return the absvalue 
        if array[absValue - 1] < 0:
            return absValue
        # map the absValue to index in the array, and
        # multiply the value at that index by -1
        array[absValue - 1] *= -1
    # no duplicates found
    return - 1