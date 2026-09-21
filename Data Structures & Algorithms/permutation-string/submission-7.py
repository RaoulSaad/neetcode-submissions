class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        hm = {}
        for i in range(len(s1)):
            hm[s1[i]] = hm.get(s1[i], 0) + 1
        l, r = 0, 0
        while r < len(s2):
            if s2[r] in hm:
                if hm.get(s2[r], 0) > 0:
                    print(s2[r], "is in hashmap")
                    hm[s2[r]] -= 1
                    if (r-l+1) == len(s1):
                        return True
                    r += 1
                else:
                    if s2[l] in hm:
                        hm[s2[l]] += 1
                    l += 1
            else:
                r+=1
                while l<r:
                    if s2[l] in hm:
                        hm[s2[l]] += 1
                    l += 1

        
        if (r-l) == len(s1):
            return True   
        return False

