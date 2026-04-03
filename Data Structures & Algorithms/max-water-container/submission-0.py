class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            if (right - left) * min(heights[left], heights[right]) > max_area:
                max_area = (right - left) * min(heights[left],heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area