class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win = len(s1)
        i = 0
        while i < len(s2) - win + 1:
            # print("".join(sorted(s1)))
            # print("".join(sorted(s2[i:i+win])))
            if "".join(sorted(s1)) == "".join(sorted(s2[i:i+win])):
                return True
            i += 1
        return False
        
