from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        i = 0
        for i, number in enumerate(nums):
            if q and q[0] < i - k + 1:
                q.popleft()
            
            while q and nums[q[-1]] < number:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                output.append(nums[q[0]])
        return output

