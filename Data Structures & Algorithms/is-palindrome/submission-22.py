class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""

        # loop thru the string and use .isalnum() 
        for letter in s:
            if letter.isalnum(): # checks if letter is alpha-numeric
                newString += letter.lower()
            
        return newString == newString[::-1]

        
        



        