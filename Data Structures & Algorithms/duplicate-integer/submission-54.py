class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set() # knowing sets cannot contain duplicates
        for i in nums:
            if i in duplicateSet:
                return True
            duplicateSet.add(i)
        return False
