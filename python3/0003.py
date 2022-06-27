class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount = 0
        for i in range(0, len(s)): # total length of string
            seen = []
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.append(s[j])
                else:
                    break
            maxcount = len(seen) if maxcount < len(seen) else maxcount
        result = maxcount
        return result
