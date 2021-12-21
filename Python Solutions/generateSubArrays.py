# 1. SubArray

# function to generate all the subarrays of a specified function 
def generatSubArrays(arr, subArrays):
    # consider all sublists starting from i 
    for i in range(len(arr)):
        # consider the sublists ending at j:
        for j in range(len(arr)):
            subArrays.append(arr[i : j + 1])


# 2. Substring 

# function to print all non-empty substrings of the specified string:
def generateSubStrings(str, subStrings):
    # consider all substrings starting from i:
    for i in range(len(str)):
        # consider all substrings ending at j:
        for j in range(i , len(str)):
            subStrings.append(str[i : j + 1])

# 3. Subsequnce:

# function to generate all possible subsequences for a given array:
def generateSubsequences(arr, index, subSequences, subArr):
    # get the subsequence whe we reach the end of the recursion tree:
    if index == len(arr):
        if len(subArr) != 0:
            subSequences.append(subArr)
            # print(subArr)
    else:
        # subsequence without including the element at the current index:
        generateSubsequences(arr, index + 1, subSequences, subArr)
        # subsequence including the element at the current index:
        generateSubsequences(arr, index + 1, subSequences, subArr + [arr[index]]) 

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    str = 'abc'
    subArrays = []
    subStrings = []
    subSequences = []
    generatSubArrays(arr, subArrays)
    generateSubStrings(str, subStrings)
    generateSubsequences(arr, 0, subSequences, [])

    print(subArrays)
    print(subStrings)
    print(subSequences)