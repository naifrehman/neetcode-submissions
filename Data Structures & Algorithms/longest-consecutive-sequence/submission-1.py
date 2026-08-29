class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                currentNum = num
                currentLength = 1

                while currentNum +1 in numSet:
                    currentNum += 1 
                    currentLength += 1

                longest = max(longest, currentLength) # set longest to a value at 
        
        return longest
                






        