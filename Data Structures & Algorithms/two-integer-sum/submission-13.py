class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in myHashMap:
                return[myHashMap[complement], index]
            else:
                myHashMap[value] = index
     