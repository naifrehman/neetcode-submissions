class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # in an anagram, the frequencies of char must be equal
        # as well as the length of the word

        # if the length of strings aren't equal, return false
        # then we sort the words and return true is equal otherwise false

        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False
