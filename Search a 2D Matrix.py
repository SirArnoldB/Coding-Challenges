class Solution(object):
    def searchMatrix(matrix, target):
        """
        :type matrix List[List[int]]
        :type target: int 
        :rtype: bool
        """

        def convertToMatrixIndex(index, matrix):
            """
            :type index: int 
            :type matrix List[List[int]]
            """
            row = index // len(matrix[0])
            col = index % len(matrix[0])
            return row, col

        # error checking for empty matrix 
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False 
        # start index and end index 
        startIndex, endIndex = 0, len(matrix) * len(matrix[0])
        while endIndex > startIndex:
            middleIndex = (startIndex + endIndex) // 2
            # conver to matrix index so that we cabn grab the element 
            matrixIndex = convertToMatrixIndex(middleIndex, matrix)

            # get the middle element 
            middleElement = matrix[matrixIndex[0]][matrixIndex[1]]

            if middleElement > target:
                endIndex = middleIndex
            elif middleElement < target:
                startIndex = middleIndex + 1 
            else:
                return True
        return False 
    
    testMatrix = [
        [1, 3, 5, 7], 
        [10, 11, 16, 20], 
        [23, 30, 34, 50]
    ]

    testTarget = 3
    print(searchMatrix(testMatrix, testTarget))
    print(searchMatrix(testMatrix, 22))
