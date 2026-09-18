class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # will skip duplicates 

            x = nums[i] # 1st var we're currently on

            left = i + 1
            right = len(nums) - 1

            while left < right:
                y = nums[left]
                z = nums[right]
                sum = x + y + z

                if sum == 0:
                    result.append([x, y, z]) # if found, append values as a list to result
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 # shift left fwd if dupliates from left side 

                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum < 0:
                    left += 1 # sum is too small and need to increment left ptr (since arr is sorted)
                
                else: 
                    right -= 1

        return result
                     

