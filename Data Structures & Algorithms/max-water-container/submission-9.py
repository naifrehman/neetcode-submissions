class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            minHeight = min(heights[left], heights[right])
            length = right - left

            area = minHeight * length

            if result < area:
                result = area
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result




        