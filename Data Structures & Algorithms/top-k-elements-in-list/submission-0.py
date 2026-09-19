class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1
        freq = freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        most_k_frequent = [item[0] for item in freq[:k]]
        return most_k_frequent