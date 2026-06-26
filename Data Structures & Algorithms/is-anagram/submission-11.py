class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # check the length of both strings
        if len(s) != len(t):
            return False

        charFreq1 = {} # dict. char: frequency
        charFreq2 = {} # also a dict with character with its frequency

        for char in s:
            charFreq1[char] = charFreq1.get(char, 0) + 1
        
        for char in t:
            charFreq2[char] = charFreq2.get(char, 0) + 1

        # now compare both dictionaies
        if charFreq1 == charFreq2:
            return True
        else:
            return False
        
        