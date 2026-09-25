class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need to add acutal values in nums as a sublist
        # each index must be used with unique set of other indices

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            x = nums[i]

            left = i + 1 # ptr starting after the x variable
            right = len(nums) - 1

            while left < right:
                y = nums[left]
                z = nums[right]
                sum = x + y + z

                if sum == 0:
                    result.append([x, y, z])
                    left += 1
                    right -= 1
                    
                    # now we want to skip duplicates in lft & right ptrs
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif sum < 0:
                    left += 1
                
                else: 
                    right -= 1
        
        return result

       





        