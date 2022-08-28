# Solution 1
class Solution:
    def getRow(self, rowIndex: int):
        """Returns the rowIndex th row of the Pascal's triangle."""
        
        def fact(num):
            """Computes the factorial of a number."""
            if num <= 0:
                return 1
            numFact = 1
            while num > 0:
                numFact *= num
                num -= 1
            return numFact
        
        # row of the Pascal's triangle
        row = []
        
        # Compute each number in the row
        for position in range(rowIndex + 1):
            num = fact(rowIndex)//(fact(position) * fact(rowIndex - position))
            row.append(num)
        return row

# Solution 2
class Solution:
    def getRow(self, rowIndex: int):
        """Returns the rowIndex th row of the Pascal's triangle."""
        
        # initialize the row with a single element 
        # since the first row only has 1 as the only element
        row = [1]
        for _ in range(rowIndex):
            # suppose we get row = [1, 3, 3, 1] from last iteration,
            # [0] + row appends 0 to the head, giving us [0, 1, 3, 3, 1]; 
            # row + [0] appends 0 to the head, giving us [1, 3, 3, 1, 0].
            # we then do element-wise addition of the 2 lists
            # zip() gives us element-wise an iterator of zipped tuples: [(0, 1), (1, 3), (3,3) (3, 1), (1, 0)]
            # finally, do the actual addition using the list comprehension, to produce: [1, 4, 6, 4, 1].
            row = [n + m for n, m in zip([0]+row, row+[0])]
        return row