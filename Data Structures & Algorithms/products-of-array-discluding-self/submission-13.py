class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currentProduct = 1
        left = [1] * len(nums)
        right = [1]*len(nums)
        # creating left array
        for i in range(len(nums)):
            left[i] = currentProduct # for index 0
            currentProduct *= nums[i]
        
        # right array
        currentProduct = 1
        for i in range(len(nums) -1, -1, -1,):
            right[i] = currentProduct
            currentProduct *= nums[i]
        
        # result array
        result = [1] * len(nums)
        for i in range(len(result)):
            result[i] = left[i] * right[i]
        
        return result








        


        
