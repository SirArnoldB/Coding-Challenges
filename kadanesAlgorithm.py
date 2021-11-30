'''

- Write a function that takes in a non-empty array of integers and returns the maximum sum that can 
- be obtained by summing up all of the integers in a non-empty subarray of the input array. 
- A subarray must only contain adjacent numbers(numbers next to each other in the input array)

'''
def kadanesAlgorithm(array):
    maxEndingHere = float('-inf')
    maxSoFar = float('-inf')

    for num in array:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar

if __name__ == '__main__':
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    arr1 = [1, 2, 3, 4, 5]
    print(kadanesAlgorithm(array))
    print(kadanesAlgorithm(arr1))
