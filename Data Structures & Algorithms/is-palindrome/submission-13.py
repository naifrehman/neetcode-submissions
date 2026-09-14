class Solution:
    def isPalindrome(self, s: str) -> bool:

        # create new string with only alpha-numeric values (Aa-Zz and 0-9)
        newString = ""

        for char in s:
            if char.isalnum():
                newString += char.lower()

        return newString == newString[::-1]