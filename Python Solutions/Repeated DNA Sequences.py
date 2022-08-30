class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Returns all the 10-letter-long sequences that occur more than once
        in DNA molecule, s.
        
        Source: https://leetcode.com/problems/repeated-dna-sequences/
        """
        # keeps track of all the sequences and their count
        sequences = {}
        
        for i in range(len(s) - 9):
            #increment the value, count, of the key in the sequences
            sequences[s[i:i+10]] = sequences.get(s[i:i+10], 0) + 1

        rep_sequences = [seq for (seq, count) in sequences.items() if count > 1]

        return rep_sequences