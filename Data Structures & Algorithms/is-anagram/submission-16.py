class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freqS = {}
        for i in s:
            freqS[i] = freqS.get(i, 0) + 1
        
        freqT = {}
        for char in t:
            freqT[char] = freqT.get(char, 0) +1

        if freqS == freqT:
            return True
        else: 
            return False


        