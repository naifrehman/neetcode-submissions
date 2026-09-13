class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       # ensure the org array (nums) contains no duplicates
       numberSet = set(nums)
       longest = 0 

       for n in numberSet:
            if (n - 1) not in numberSet:
                length = 1
                while (n + 1) in numberSet:
                    length += 1
                    n += 1
                longest = max(length, longest)
        
       return longest


       
                






        