class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need to add acutal values in nums as a sublist
        # each index must be used with unique set of other indices

        nums.sort() # sort the nums array [-1, -1, 0, 1, 2, 4]
        result = [] # going to add sublists within this result list

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            x = nums[i] # our first value of 3sum

            left = i + 1
            right = len(nums) -1

            while left < right:
                y = nums[left]
                z = nums[right]
                currSum = x + y + z

                # we've found a 3 num pair
                if currSum == 0:
                    result.append([x, y, z])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
                
        return result




            

        

       
       





        