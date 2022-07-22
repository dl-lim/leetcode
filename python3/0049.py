class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sw = ''.join(sorted(word))
            if not d.get(sw):
                d[sw] = []
            d[sw].append(word)
        return d.values()