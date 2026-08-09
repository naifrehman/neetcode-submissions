class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set() # create a set, b/c there will be no duplicates
        for i in range(len(nums)): # loop through the nums arr
            if nums[i] in numberSet: # checks if i @ each index is in set
                return True # if condition, yes, true
            else:
                numberSet.add(nums[i]) # if not in numberSet, i must be unique, add to set
        return False
