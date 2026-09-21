class Solution:
    def maxArea(self, heights: List[int]) -> int:
        watah = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            capacity = (j - i) * min(heights[i], heights[j])
            if capacity > watah:
                watah = capacity
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return watah