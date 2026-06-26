class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # run 2 nested for loops that checks the 1st index
        # with every other index, and if the sum == target
        # return the 2 index 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]
