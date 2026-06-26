class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value: index
        for index, value in enumerate(nums):
            complement = target - value # complement is a value
            if complement in hashmap:
                return [hashmap[complement], index] # hmap[compmement] returns a index
            else:
                hashmap[value] = index

            
        