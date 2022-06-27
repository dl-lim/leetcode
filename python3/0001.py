class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value

            if remaining in seen:
                return [seen[remaining], i]

            seen[value] = i

            
