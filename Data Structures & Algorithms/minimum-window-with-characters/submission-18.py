class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        hm = {}
        for c in t:
            hm[c] = hm.get(c, 0) + 1
        win_size = 100001
        l,r = 0, 0
        output = ""
        l_best = -1
        r_best = -1
        while r < len(s):
            if s[r] not in hm:
                if l == r:
                    l += 1
                    r += 1
                    continue
                else:
                    r += 1
            else:
                if hm[s[r]] <= 0:
                    hm[s[r]] -= 1
                    if all(value <= 0 for value in hm.values()):
                        if win_size > r-l:
                            l_best = l
                            r_best = r
                            win_size = r-l
                    # if s[l] == s[r]:
                    while (s[l] not in hm or hm[s[l]] < 0) and l < r:
                        
                        if s[l] in hm:
                            # print(s[l], "is at", hm[s[l]])
                            hm[s[l]] += 1
                            # print(s[l], "is now at", hm[s[l]])
                            # else:
                            #     break
                        l += 1
                    # else:
                    #     hm[s[r]] -= 1      
                else:
                    hm[s[r]] -= 1
                r += 1

                if all(value <= 0 for value in hm.values()):
                    if win_size > r-l:
                        r_best = r
                        l_best = l
                        win_size = r-l
                        
        if all(value <= 0 for value in hm.values()) and win_size > r-l:
            r_best = r
            l_best = l
        if r_best != -1 and l_best != -1:
            output = s[l_best:r_best]
        return output
                        
