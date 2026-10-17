class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            # adjust subString by removing duplicates
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right]) # once all duplicates remved + adjusted
            result = max(result, len(charSet))

        return result
            





        