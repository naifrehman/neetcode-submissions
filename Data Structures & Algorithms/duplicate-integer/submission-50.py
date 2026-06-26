class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set() # create an empty set
        for i in range(len(nums)):
            if nums[i] in numberSet: # if num exists in set
                return True          # return True
            else:
                numberSet.add(nums[i]) # otherwise, add it to the set
        return False                   