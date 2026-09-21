class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest = 1
        current_streak = 1
        current_element = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == current_element + 1:
                current_streak += 1
            elif nums[i] == current_element:
                pass
            else:
                if current_streak > longest:
                    longest = current_streak
                current_streak = 1
            current_element = nums[i]
        if longest < current_streak:
            longest = current_streak
        return longest
                