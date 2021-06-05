"""
### Find Three Largest Numbers
-------------------------------
Source: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three
largest integers in the input array. The function should return duplicate integers if necessary; for example, it should return
[10, 10, 12] for an input array of [10, 5, 9, 10, 12] .
"""

'''
Solution
********
'''
# O(n) - time | O(1) - space : where n is the length of the array
def findThreeLargestNumbers(array):
    '''
    # Planning the Algorithm: 
    - define three var to hold the three largest numbers
    - assign these to the first three elements in the array
    - place these numbers in such a way that the first-number is the largest, followed by the second, then the third
    - Then, iterate through the array, starting at i = 3. 
    - for each element, check if its greater than the largest of the three numbers, if not, check the second, if not, check the third
    - when the current number in the array is greater than the first number ( our largest number) - update the largest number, 
    - if its greater than the second largest number, update the second largest number, 
    - else if its greater than the smallest number, third number, update the third number,
    - else - just continue 
    '''
    # first group the first three elements in the array from largest to smallest
    a = array[0] 
    b = array[1]
    c = array[2]
    
    if (a >= b) and (a >= c):
        # largest of the first three elements 
        firstValue = a
        # secondValue - second largest number | thirdValue - third largest number ( smallest number)
        secondValue, thirdValue = checkLargest(b,c)
            
    elif (b >= a) and (b >= c):
        # 
        firstValue = b
        secondValue, thirdValue = checkLargest(a,c)
    else:
        firstValue = c
        secondValue, thirdValue = checkLargest(b,a)
    
    i = 3
    while i < len(array):
        if array[i] > firstValue:
            # if the current number is greater than firstValue, assign it to be the firstValue
            # and update the third and second values as well
            thirdValue, secondValue, firstValue = secondValue, firstValue, array[i]
        elif array[i] < firstValue and array[i] > secondValue:
            # if the current number if between firstValue and secondValue, assign it to be the secondValue
            # and update the third value as well
            thirdValue, secondValue = secondValue, array[i]
        elif array[i] < secondValue and array[i] > thirdValue:
            # if the current number is between the secondValue and the thirdValue, assign it to be the thirdValue
            thirdValue = array[i]
        i += 1
    return [thirdValue, secondValue, firstValue]
    
# checkLargest return a tuple in the form: largest, smallest, given two values x and y
def checkLargest(x, y):
    if x > y:
        return x, y
    else:
        return y, x


'''
Solution 2:
************
'''
# O(n) - time | O(1) - space : where n is the length of the array
def findThreeLargestNumbers(array):
    # we start with an empty array of three largest numbers
    # then, as we iterate through the array, we update the value of the numbers in the array
    # depending on the number that we currently have
    threeLargest = [None, None, None]
    for num in array:
        # calle the helper method
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    # firstly, compare the current number to the third value
    # in the threeLargest array
    if threeLargest[2] is None or num > threeLargest[2]:
        # update the value 
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        # update the value
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        # update the value 
        shiftAndUpdate(threeLargest, num, 0)
#@param array - the threeLargest array
#@param num - the number that we want to insert or update into the array
#@param idx - the last index in our array of three numbers that we want to update
def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            # update the array
            array[i] = num
        else:
            array[i] = array[i + 1]