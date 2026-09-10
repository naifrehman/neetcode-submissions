class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = "" # words in a list to 1 string
        for word in strs:
            encodedString += str(len(word)) + "#" + word
        return encodedString

    def decode(self, s: str) -> List[str]:

        # encoded will give us int#word1int#word2
        # need to return back a string

        # for ex. "5#apple3#fig"

        result = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # from i (0) to but not including j, to only read number and convert to int
            result.append(s[j+1:1+length+j])

            i = j + length + 1

        return result
            



