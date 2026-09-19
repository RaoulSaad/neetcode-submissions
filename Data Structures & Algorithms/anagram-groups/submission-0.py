class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mlems = {}
        for str in strs:
            str_sort = "".join(sorted(str))
            if str_sort not in mlems:
                mlems[str_sort] = [str]
            else:
                mlems[str_sort].append(str)
        output = []
        for key in mlems:
            output.append(mlems[key])
        return output