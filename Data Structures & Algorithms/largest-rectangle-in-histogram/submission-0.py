from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        span_l = [-1]*len(heights)
        span_r = [-1]*len(heights)

        stack = deque()
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                span_r[stack[-1]] = i
                stack.pop()
            stack.append(i)
        # print(span_r)
        stack.clear()
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                span_l[stack[-1]] = i
                stack.pop()
            stack.append(i)
        # print(span_l)

        max_area = float('-inf')
        outbounds = False
        for i in range(len(heights)):
            outbounds = False
            if span_l[i] == -1:
                left = 0
                outbounds = True
            else:
                left = span_l[i]
            if span_r[i] == -1:
                right = len(heights)
            else:
                right = span_r[i]
            if outbounds:
                width = right - left
            else:
                width = right - left - 1
            # print(width, heights[i])
            area = width * heights[i]
            if max_area < area:
                max_area = area
        return max_area