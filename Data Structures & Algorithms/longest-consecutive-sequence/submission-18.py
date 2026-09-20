class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # ensure no duplicates
        numSet = set(nums)
        longest = 0

        # iterate thru the array
        for value in numSet:
            if value - 1 not in numSet:
                currentLength = 1
                currentValue = value
                
                while currentValue + 1 in numSet:
                    currentLength += 1
                    currentValue += 1 # move to next val & check if in nums
                longest = max(longest, currentLength)
        
        return longest
                






        