from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stacc = deque()
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stacc.append(c)
            else:
                if stacc:
                    opener = stacc.pop()
                else:
                    return False
                if (c == ")" and opener != "(") or (c == "]" and opener != "[") or (c == "}" and opener != "{"):
                    return False
        if stacc:
            return False
        return True