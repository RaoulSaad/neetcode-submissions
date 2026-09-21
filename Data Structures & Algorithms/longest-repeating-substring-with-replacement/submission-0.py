class Solution:
    def most_frequent(self, count: dict) -> int:
        most_freq = 0
        for key in count:
            if most_freq < count[key]:
                most_freq = count[key]
        return most_freq
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        count = {}
        l,r=0,0
        res = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            most_freq = self.most_frequent(count)
            if (r-l+1) - most_freq <= k:
                r += 1
            else:
                if res < r-l:
                    res = r-l
                while (r-l+1) - most_freq > k:
                    count[s[l]] -= 1
                    most_freq = self.most_frequent(count)
                    l += 1
                r += 1

        if res < r-l:
            res = r-l
        return res
                        
           

            

