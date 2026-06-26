class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if both strings are identical in length
        if len(s) != len(t):
            return False
        
        s1 = sorted(s)
        t1 = sorted(t)

        if s1 == t1:
            return True
        else:
            return False
        
        