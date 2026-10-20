class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maximumArea = 0
        while left < right:
            height = min(heights[right], heights[left])
            width = right - left
            area = height * width

            if (area > maximumArea):
                maximumArea = area
            elif (heights[right] > heights[left]):
                left += 1
            else:
                right -= 1
        
        return maximumArea


        