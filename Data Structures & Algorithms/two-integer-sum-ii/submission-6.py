class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # nums array --> sorted in increasing order
        # return a list indexes of 2 nums --> that add to the target

        left = 0
        right = len(numbers) - 1

        result = [] # will hold the 2 numbers

        while left < right:
            if (numbers[left] + numbers[right] == target):
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif (numbers[left] + numbers[right] < target):
                left += 1
            elif (numbers[left] + numbers[right] > target):
                right -= 1
            
            else:
                return result
        