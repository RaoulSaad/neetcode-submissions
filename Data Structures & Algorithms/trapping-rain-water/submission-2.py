class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        greater_left = []
        greater_right = []
        max_height = 0
        for i in range(len(height)):
            greater_left.append(max_height)
            if height[i] >= max_height:
                max_height = height[i]
        max_height = 0
        for i in range(len(height)-1, -1, -1):
            greater_right.append(max_height)
            if height[i] >= max_height:
                max_height = height[i]
        greater_right.reverse()

        trapped = 0
        for i in range(len(height)):
            trapped += max(0, min(greater_left[i], greater_right[i])-height[i])

        return trapped
            
