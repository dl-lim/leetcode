class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chk = list(set(nums))
        result = len(chk) != len(nums)
        return result
