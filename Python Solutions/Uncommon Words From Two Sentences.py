'''
# Uncommon Words from Two Sentences
-----------------------------------
Source: https://leetcode.com/problems/uncommon-words-from-two-sentences/
- A sentence is a string of single-space separated words where each word consists only of lowercase letters.
- A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
- Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example 1:
    # Input: s1 = "this apple is sweet", s2 = "this apple is sour"
    # Output: ["sweet","sour"]
# Example 2:
    # Input: s1 = "apple apple", s2 = "banana"
    # Output: ["banana"]

# Constraints:
    # 1 <= s1.length, s2.length <= 200
    # s1 and s2 consist of lowercase English letters and spaces.
    # s1 and s2 do not have leading or trailing spaces.
    # All the words in s1 and s2 are separated by a single space.
'''
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Algorithm
        # create a hashtable to keep track of the count of all the words, 
        # loop through the two sentences and add the words to the hashtable, 
        # loop through the key value pairs in the hashtable and return those with a count of one
        
        # keeps track of the mapping of each word to its count
        wordCount = {}
        
        # loop through the first sentence
        for word in s1.split(" "):
            wordCount[word] = wordCount.get(word, 0) + 1
        
        # loop through the second sentence 
        for word in s2.split(" "):
            wordCount[word] = wordCount.get(word, 0) + 1
        
        # keeps track of the wors with a count of 1
        uncommon = []
        
        # get the uncommon words
        for word, count in wordCount.items():
            if count == 1:
                uncommon.append(word)
        return uncommon