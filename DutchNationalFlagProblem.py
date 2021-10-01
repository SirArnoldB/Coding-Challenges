'''
Given an array containing only 0's, 1's, and 2's, sort it in linear time and using constant space

Input: [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2,]

'''

def swap(A, i , j):
    print(i, j, A)
    A[i], A[j] = A[j], A[i]

# linear time partition routine to sort a list containing 0, 1, and 2
# It is similar to 3-way partitioning for the Dutch National Flag Problem
def threeWayPartition(A):
    start = mid = 0
    pivot = 1
    end = len(A) - 1

    while mid <= end:
        if A[mid] < pivot:  # current element is 0
            swap(A, start, mid)
            start += 1
            mid += 1
        elif A[mid] > pivot:    # current element is 2
            swap(A, mid, end)
            end -= 1
        else:                   # current element is 1
            mid = mid + 1

if __name__ == '__main__':
    A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    threeWayPartition(A)
    print(A)