class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if both strings are identical in length
        if len(s) != len(t):
            return False
        
        # use hashmap to count freq of each char in s1
        charCount = {}

        for char in s:
            charCount[char] = charCount.get(char, 0) + 1

        # iterate thru the 2nd string
        for char in t:
            charCount[char] = charCount.get(char, 0) - 1

        # now check if the occurances of all char == 0:
        for value in charCount.values():
            if value!= 0:
                return False
        return True

        
        
        