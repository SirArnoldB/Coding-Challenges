'''
Run-Length Encoding
-------------------
Source: https://www.algoexpert.io/questions/Run-Length%20Encoding

- Write a function that takes in a non-empty string and returns its run-length encoding.
- From Wikipedia, "run-length encoding is a form of lossless data compression in which
- runs of data are stored as a single data value and count, rather than as the original run." 
- For this problem, a run of data is any sequence of consecutive, identical characters. 
- So the run "AAA" would be run-length-encoded as "3A".

- To make things more complicated, however, the input string can contain all sorts of special
- characters, including numbers. And since encoded data must be decodable, this means
- that we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA"
- (12 A s), can't naively be encoded as "12A", since this string can be decoded as either
- "AAAAAAAAAAAA" or "1AA" . Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned
- run should be encoded as "9A3A".

# Sample Input
    # string = "AAAAAAAAAAAAABBCCCCDD"

# Sample Output
    # "9A4A2B4C2D"
'''
# O(n) - time | O(n) - space - where n is the length of the input string
def runLengthEncoding(string):
	# keeps track of the characters, 
	# strings are imutable, charList can be mutated 
    charList = []
    i = 0
    while i < len(string):
        count = 0
		# current character
        char = string[i]
		# count the number of adjacent occurences of the character in the string 
        while i < len(string) and string[i] == char:
            count += 1
            i += 1
		# evaluate the count and add the character to the character list 
        if count <= 9:
            charList.append("{0}{1}".format(count, char))
        else:
            if count % 9 == 0:
                count = (count // 9)
                charList.append("{0}{1}".format(9, char) * count)
            else:
                countOne = (count // 9)
                countTwo = count % 9
                charList.append("{0}{1}".format(9, char) * countOne)
                charList.append("{0}{1}".format(countTwo, char))
    # return a joined string of the characters in charList
    return "".join(charList)

# Driver Code 

if __name__ == "__main__":
    print("Test Case 1")
    print(runLengthEncoding(string = 'AAAAAAAABBBBBBtteeyuuz'))