class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # i is the string
        # j is the letter
        # k is a placeholder matrix
        strs = sorted(strs, key = lambda x : len(x))
        result = ""

        for i in range(0,len(strs[0])): # iterate horizontally in each word
            for j in range(1,len(strs)): # iterate each word in list
                if strs[0][i] != strs [j][i]:
                    return result
            result += strs[0][i]
        return result
