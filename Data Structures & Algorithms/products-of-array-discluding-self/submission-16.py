class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        right = [1] * len(nums)

        # creating left array
        currentProduct = 1
        for i in range(len(nums)):
            left[i] = currentProduct
            currentProduct *= nums[i]

        # creating right array
        currentProduct = 1
        for i in range(len(nums) -1, -1, -1):
            right[i] = currentProduct
            currentProduct *= nums[i]
        
        # final result array
        result = [1] * len(nums)
        for i in range(len(result)):
            result[i] = left[i] * right[i]

        return result

        

        
        







        


        
