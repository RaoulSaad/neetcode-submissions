class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded = encoded + str(len(st)) + "#" + st
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_size = int(s[i:j])
            i = j
            strs.append(s[i+1:i+str_size+1])
            i += str_size + 1
        return strs

