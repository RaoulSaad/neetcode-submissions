class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(n):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * nums[i-1]
        i = n-1

        while i >= 0:
            if i == n-1:
                i -= 1
                continue
            suffix[i] = suffix[i+1] * nums[i+1]
            i -= 1

        for i in range(n):
            prefix[i] = prefix[i] * suffix[i]
        
        return prefix
        
