class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputs = set()
        for i in range(len(nums)):
            x = nums[i]
            j = i+1
            k = len(nums) - 1
            while j < k:
                if x + nums[j] + nums[k] == 0:
                    outputs.add(tuple([x, nums[j], nums[k]]))
                    j += 1
                elif x + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return [list(t) for t in outputs]
            
