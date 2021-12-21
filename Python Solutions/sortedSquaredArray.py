'''

Sorted Squared Array:
---------------------
    # Write a function that takes in a non-empty array of integers that are sorted in ascending
    # order and returns a new array of the same length with the squares of the original
    # integers also sorted in ascending order.

'''
# O(n) time | O(n) space - where n is the length of the input array

# @param array the list of integers
# @return list of the squares of the original integers in array
def sortedSquaredArray(array):
    # pointers to keep track of the largest and the smallest values
    smallest_value_idx, largest_value_idx = 0, len(array)-1
    
    # output array
    squares_array = []
    
    # traverse the list, 
    # for each iteration, compare the values at the smallest_idx and largest_idx
    # insert the square of the largest value into the output array, 
    # and update the corresponding counter
    while smallest_value_idx <= largest_value_idx:
        
        smallestValue = array[smallest_value_idx] ** 2
        largestValue = array[largest_value_idx] ** 2
        
        if smallestValue > largestValue:
            squares_array.append(smallestValue)
            smallest_value_idx += 1
        else:
            squares_array.append(largestValue)
            largest_value_idx -= 1
    
    return squares_array[::-1]

if __name__ == '__main__':
    array = [-100, -3, -2, 0, 1,5, 7, 8, 9, 90]
    print(sortedSquaredArray(array))