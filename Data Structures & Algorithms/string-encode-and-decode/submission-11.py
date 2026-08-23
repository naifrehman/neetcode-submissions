class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        


    def decode(self, s: str) -> List[str]:
        # given str as encoded string in: int#word1int2#word2
        # must return back a list

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            # from 0 to 2nd position of string but not including reads the first #   letter - which is the number in str format converted to int
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res


      




