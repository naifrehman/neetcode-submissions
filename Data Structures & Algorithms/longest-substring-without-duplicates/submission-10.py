class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        chars = set()

        for right in range(len(s)):
            # while char at right in set, remove from left
            while s[right] in chars:  
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            result = max(result, right - left + 1)

        return result






        