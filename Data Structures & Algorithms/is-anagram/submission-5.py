class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # brute force solution requires to sort both strings
        # then we compare 

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        else:
            return False
        