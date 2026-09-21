class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hash_map = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] not in hash_map:
                hash_map[s[j]] = j
                j += 1
            elif hash_map[s[j]] < i:
                hash_map[s[j]] = j
                j += 1
            else:
                if j - i > max_len:
                    print("New max len:", j - i, j, i)
                    max_len = j - i
                i = hash_map[s[j]] + 1
                hash_map[s[j]] = j
                j += 1
        if j - i > max_len:
            print(i, j)
            max_len = j - i 
        return max_len



        