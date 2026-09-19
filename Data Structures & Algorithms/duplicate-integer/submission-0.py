class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
                if counter[i] > 1:
                    return True
            else:
                counter[i] = 1
        return False