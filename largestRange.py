"""
Largest Range
--------------
- Write a function that takes in an array of integers and returns an array of length 2 representing
- the largest range of integers contained in that array.
- The first number in the output array should be the first number in the range, while the second
- number should be the last number in the range.
- A range of numbers is defined as a set of numbers that come right after each other in the set of
- real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6} ,
- which is a range of length 5. Note that numbers don't need to be sorted or adjacent in the input
- array in order to form a range.
- You can assume that there will only be one largest range.

# Sample Input
    # array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# Sample Output
    # [0, 7]

"""


# O(nlogn) - time | O(1) - space: where n is the number of elements in the array
def largestRange(array):
    # sort the numbers in ascending order
    array.sort()
    largeRange = [0, 0]
    idx = 0
    while idx < len(array):
        # startIdx points to the first element in this range
        # start is the starting element in this range.
        start, startIdx = array[idx], idx
        while (idx < len(array) - 1) and (array[idx] + 1 == array[idx + 1]
                                          or array[idx] == array[idx + 1]):
            idx += 1
        # endIdx now points to the last element in this range
        # end is the last element of this range
        end, endIdx = array[idx], idx
        # special case - startIdx equals endIdx
        if startIdx == endIdx:
            largeRange = [start, end] if largeRange == [0, 0] else largeRange
        largeRange = [
            start, end
        ] if (end - start) > (largeRange[1] - largeRange[0]) else largeRange
        idx += 1
    return largeRange
