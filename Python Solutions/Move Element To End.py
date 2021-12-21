'''
# Move Element To End
-------------------
Source: https://www.algoexpert.io/questions/Move%20Element%20To%20End

- You're given an array of integers and an integer.
- Write a function that moves all instances of that
- integer in the array to the end of the array and returns the array.
- The function should perform this in place (i.e., it
- should mutate the input array) and doesn't need
- to maintain the order of the other integers.

# Sample Input
    # array = [2, 1, 2, 2, 2, 3, 4, 2]
    # toMove = 2
# Sample Output
    # [1, 3, 4, 2, 2, 2, 2, 2]
'''
### Solution 1
# O(n) - time | O(1) - space : where n is the length  of the array
def moveElementToEnd(array, toMove):
    """
    :type array List[int]
    :type toMove int
    :rtype List[int]
    """
    # declare the pointer that we will be moving inwards in the array
    left = 0
    right = len(array) - 1
    
    # move the pointers inwards, and 
    # progressively check if we should swap values 
    while left < right: # traversed the entire array
        while array[right] == toMove and left < right:
            # decrement the right by 1
            right -= 1
        # check the value at the left index
        if array[left] == toMove:
            # peform a sawp
            array[left], array[right] = array[right], array[left]
        left += 1
    return array

# *********************************************************** #

### Solution 2
# O(n) - time | O(1) - space : where n is the length of the input array
def moveElementToEnd(array, toMove):
    # keeps track of the current index 
    counter = 0
    # get the length of the array
    lenArr = len(array)
    # keeps track of the number of toMove elements
    # that have been move to the end of the array
    moves = 0
    # counter < (lenArr - moves - 1) makes sure that we don't 
    # mover elements that have already been moved
    # keeps track of the last index of the original array where we shoudl stop
    while counter < lenArr - moves - 1:
        if array[counter] == toMove:
            # remove the element
            array.pop(counter)
            # append it to the end of the array
            array.append(toMove)
            # advance the number of moves 
            moves += 1
        # check if the current index contains toMove
        if array[counter] == toMove: 
            # do not advance the counter 
            counter += 0
        else: 
            # otherwise, increment the counter 
            counter += 1
    # return the mutated array
    return array

