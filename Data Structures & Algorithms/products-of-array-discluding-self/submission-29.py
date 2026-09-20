class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
     left = [1] * len(nums)
     right = [1] * len(nums)

     # populate the left array
     leftMultiplier = 1
     for i in range(len(nums)):
        left[i] = leftMultiplier
        leftMultiplier *= nums[i]
    
     # populate the right array
     rightMultiplier = 1
     for i in range(len(nums) -1, -1, -1):
         right[i] = rightMultiplier
         rightMultiplier *= nums[i]
    
     # result array
     result = [1] * len(nums)
     for i in range(len(result)):
         result[i] = left[i] * right[i]
    
     return result

        

        
        







        


        
